# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-05-09 21:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfoliosite', models.CharField(blank=True, max_length=100)),
                ('profilepic', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Testuser',
        ),
    ]
