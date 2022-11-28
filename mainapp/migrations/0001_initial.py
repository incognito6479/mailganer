# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-28 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'SentEmailList',
                'verbose_name_plural': 'SentEmailLists',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surename', models.CharField(max_length=256)),
                ('birth_date', models.DateField()),
                ('email', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='TemplateName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=256)),
                ('template_name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'TemplateName',
                'verbose_name_plural': 'TemplateName',
            },
        ),
        migrations.AddField(
            model_name='sentemaillist',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Subscriber'),
        ),
        migrations.AddField(
            model_name='sentemaillist',
            name='template_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TemplateName'),
        ),
    ]
