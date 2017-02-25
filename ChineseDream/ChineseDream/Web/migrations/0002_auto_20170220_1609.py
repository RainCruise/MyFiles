# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-20 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infomation_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('eamil', models.CharField(max_length=50, verbose_name='Email')),
                ('number', models.CharField(max_length=50, verbose_name='Number')),
                ('apply_for', models.CharField(max_length=50, verbose_name='Apply')),
                ('message_content', models.TextField(verbose_name='CONTENTS')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='contact',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]