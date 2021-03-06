# Generated by Django 2.0.2 on 2018-03-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20180308_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='所在公司'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_title',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='工作职位'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='my_home',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='登录后首页跳转'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='website',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='个人网站'),
        ),
    ]
