# Generated by Django 3.2.12 on 2022-03-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name_der_praxis',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]