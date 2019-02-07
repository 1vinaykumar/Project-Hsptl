# Generated by Django 2.1.5 on 2019-02-05 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20190205_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_dat', models.DateField(default=datetime.datetime.today)),
                ('slots', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_ref',
            field=models.CharField(default='v', max_length=50),
        ),
    ]
