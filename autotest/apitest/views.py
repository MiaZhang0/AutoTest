from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from apitest.models import Apitest, Apistep, Apis
import HTMLTestRunner
import pymysql


# Create your views here.
# 登录
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
        # 俩部分等价
        # else:
        #     context = {'error':'username or password error'}
        #     return render(request, 'login.html', context=context)
    return render(request, 'login.html')


# 首页
def home(request):
    return render(request, 'home.html')


# 退出
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()  # 读取所有流程接口数据
    username = request.session.get('user', '')  # 读取浏览器登录Session
    # 定义流程接口数据的变量并返回到前端
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})


@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = Apistep.objects.all()
    return render(request, 'apistep_manage.html', {'user': username, 'apisteps': apistep_list})


# 单一接口测试
@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    return render(request, 'apis_manage.html', {'user': username, 'apiss': apis_list})


# 测试报告
@login_required
def test_report(request):
    db = pymysql.connect('127.0.0.1', 'root', 'Zz1!@#$%', 'autotest')
    cursor = db.cursor()
    sql1 = '''select count(id) from apitest_apis where apitest_apis.apistatus=1'''
    aa = cursor.execute(sql1)
    db.commit()
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = '''select count(id) from apitest_apis where apitest_apis.apistatus=0'''
    bb = cursor.execute(sql2)
    db.commit()
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()  # 统计接口数
    return render(request, 'report.html', {'user': username, 'apiss': apis_list, 'apiscounts': apis_count,
                                           'apis_pass_counts': apis_pass_count, 'apis_fail_counts': apis_fail_count})
