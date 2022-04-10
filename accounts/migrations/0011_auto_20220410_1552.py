# Generated by Django 3.2.12 on 2022-04-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220410_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fachrichtung',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name_der_praxis',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='postleitzahl',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='strasse',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='strasse_nr',
            field=models.IntegerField(null=True),
        ),
    ]