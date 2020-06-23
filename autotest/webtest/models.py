from django.db import models
from product.models import Product


# Create your models here.
# 创建Web用例管理功能模块
class Webcase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    webcasename = models.CharField('用例名称', max_length=200)  # 测试用例名称
    webtestresult = models.BooleanField('测试结果')  # 测试结果
    webtester = models.CharField('测试负责人', max_length=16)  # 测试执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'web测试用例'
        verbose_name_plural = 'web测试用例'

    def __str__(self):
        return self.webcasename


class Webcasestep(models.Model):
    # objects = None
    Webcase = models.ForeignKey(Webcase, on_delete=models.CASCADE, null=True)  # 关联接口ID
    webteststep = models.CharField('测试步骤', max_length=200)  # 测试步骤
    webcasename = models.CharField('测试用例标题', max_length=200,null=True)  # 测试用例标题
    webtestobjname = models.CharField('测试对象名称描述', max_length=200)  # 测试对象名称描述
    webfindmethod = models.CharField('定位方式', max_length=200)  # 定位方式
    webevelement = models.CharField('控件元素', max_length=800)  # 控件元素
    weboptmethod = models.CharField('操作方法', max_length=200)  # 操作方法
    webtestdata = models.CharField('测试数据', max_length=200, null=True)  # 测试数据，临时增加字段时要设置可为空
    webassertdata = models.CharField('验证数据', max_length=200)  # 验证数据
    create_time = models.DateTimeField('创建时间')  # 创建时间，自动获取当前时间
    webtestresult = models.BooleanField('测试结果')  # 测试结果


    def __str__(self):
        return self.webteststep
