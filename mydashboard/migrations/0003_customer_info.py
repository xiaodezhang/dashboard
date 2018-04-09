# Generated by Django 2.0 on 2018-04-08 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydashboard', '0002_waiter_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydashboard.person')),
            ],
        ),
    ]
