# Generated by Django 2.1.5 on 2019-02-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_appointment_app_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='app_user',
            field=models.CharField(default='v', max_length=50),
        ),
    ]
