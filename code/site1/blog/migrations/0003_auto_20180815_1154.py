# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_date'], 'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c', 'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438'},
        ),
    ]