from django.db import models
from product.models import Product


# Create your models here.
# bug管理功能模块
class Bug(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    bugname = models.CharField('bug名称', max_length=64)  # bug名称
    bugdetail = models.CharField('详情', max_length=200)  # bug详情
    BUG_STATUS = (('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭'))
    bugstatus = models.CharField(verbose_name='解决状态', choices=BUG_STATUS, default='激活', max_length=200,
                                 null=True)  # 解决状态
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
    buglevel = models.CharField(verbose_name='严重程度', choices=BUG_LEVEL, default='3', max_length=200, null=True)  # 严重程度
    BUG_PRIORITY = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
    bugpriority = models.CharField(verbose_name='优先级',choices=BUG_PRIORITY,default='3',max_length=200,null=True) # bug优先级
    bugcreater = models.CharField('创建人', max_length=200)  # 创建人
    bugassign = models.CharField('指派给', max_length=200)  # 指派给
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间

    class Meta:
        verbose_name = 'bug管理'
        verbose_name_plural = 'bug管理'

    def __str__(self):
        return self.bugname
