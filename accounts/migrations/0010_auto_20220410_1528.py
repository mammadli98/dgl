# Generated by Django 3.2.12 on 2022-04-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20220410_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='anmerkungen',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ansprechpartner',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='arzt',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='groese_praxis',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mitarbeiter',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='raume',
            field=models.IntegerField(null=True),
        ),
    ]
