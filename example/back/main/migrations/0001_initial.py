# Generated by Django 3.1 on 2022-09-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat', models.IntegerField()),
                ('char', models.CharField(default='null', max_length=16)),
            ],
        ),
    ]
