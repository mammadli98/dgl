# Generated by Django 3.2.12 on 2022-04-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220410_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='arzt',
        ),
    ]
