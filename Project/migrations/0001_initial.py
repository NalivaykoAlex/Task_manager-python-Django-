# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-05 08:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_off', models.DateTimeField(blank=True, null=True)),
                ('assigned_to_user', models.ForeignKey(default='', max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='userm', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default='', max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
