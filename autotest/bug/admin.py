from django.contrib import admin
from bug.models import Bug


# Register your models here.
# 注册bug管理模块
class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname', 'bugdetail', 'bugstatus', 'buglevel', 'bugpriority', 'bugcreater', 'bugassign',
                    'create_time', 'id']


# 把bug管理模块注册到Django admin后台并能显示
admin.site.register(Bug)
