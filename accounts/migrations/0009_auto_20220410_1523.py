# Generated by Django 3.2.12 on 2022-04-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220410_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='anmerkungen',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='arzt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groese_praxis',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='raume',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
