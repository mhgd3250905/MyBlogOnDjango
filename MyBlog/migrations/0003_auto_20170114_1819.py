# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 10:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0002_auto_20170114_1757'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='SKBlog',
        ),
    ]
