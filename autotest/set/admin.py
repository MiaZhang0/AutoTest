from django.contrib import admin
from set.models import Set


# Register your models here.
# 注册系统设置功能模块
class SetAdmin(admin.ModelAdmin):
    list_display = ['setname', 'setvalue', 'id']


# 把系统设置模块注册到Django admin后台并显示
admin.site.register(Set)
