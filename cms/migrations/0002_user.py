# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='ユーザー名', max_length=255)),
                ('account', models.CharField(verbose_name='本名', max_length=255)),
                ('password', models.CharField(verbose_name='パスワード', max_length=255)),
                ('mail_address', models.CharField(verbose_name='メールアドレス', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
