# Generated by Django 4.1.1 on 2022-09-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_postdata_posttime_alter_reviewdata_reviewtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='loginTime',
            field=models.CharField(default=-1, max_length=114514),
        ),
    ]
