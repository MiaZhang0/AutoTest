# Generated by Django 3.0.6 on 2020-06-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0002_remove_webcasestep_webcasename'),
    ]

    operations = [
        migrations.AddField(
            model_name='webcasestep',
            name='webcasename',
            field=models.CharField(max_length=200, null=True, verbose_name='测试用例标题'),
        ),
    ]
