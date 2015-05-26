# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe7\xbe\xa4\xe5\x90\x8d\xe5\xad\x97')),
                ('group_number', models.CharField(max_length=25, verbose_name=b'\xe7\xbe\xa4\xe5\x8f\xb7\xe7\xa0\x81')),
                ('qq', models.CharField(max_length=25, verbose_name=b'QQ\xe5\x8f\xb7')),
                ('nick', models.CharField(max_length=64, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('sex', models.CharField(max_length=20, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('position', models.CharField(max_length=20, verbose_name=b'\xe7\xbe\xa4\xe8\x81\x8c\xe4\xbd\x8d')),
            ],
            options={
                'db_table': 'qq_group',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QQInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qq', models.CharField(max_length=25, verbose_name=b'QQ\xe5\x8f\xb7')),
                ('nick', models.CharField(max_length=64, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('sex', models.CharField(max_length=20, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('position', models.CharField(help_text=b'\xe6\x88\x90\xe5\x91\x98;\xe5\x88\x9b\xe5\xa7\x8b\xe4\xba\xba;\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', max_length=20, verbose_name=b'\xe7\xbe\xa4\xe8\x81\x8c\xe4\xbd\x8d')),
                ('group_number', models.CharField(max_length=25, verbose_name=b'\xe7\xbe\xa4\xe5\x8f\xb7\xe7\xa0\x81')),
            ],
            options={
                'db_table': 'qq_info',
            },
            bases=(models.Model,),
        ),
    ]
