# Generated by Django 3.2.12 on 2022-04-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20220410_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='anmerkungen',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ansprechpartner',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='arzt',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='groese_praxis',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mitarbeiter',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='raume',
        ),
    ]