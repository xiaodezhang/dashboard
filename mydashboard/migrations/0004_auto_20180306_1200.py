# Generated by Django 2.0 on 2018-03-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydashboard', '0003_auto_20180306_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='area',
            field=models.CharField(max_length=50, null=True, verbose_name='区域'),
        ),
    ]