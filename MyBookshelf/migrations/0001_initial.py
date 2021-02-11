# Generated by Django 2.1.15 on 2021-02-11 04:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='Kakeibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='日付')),
                ('money', models.IntegerField(help_text='単位は日本円', verbose_name='金額')),
                ('quantity', models.IntegerField(default=0, verbose_name='数量')),
                ('memo', models.CharField(max_length=500, verbose_name='メモ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyBookshelf.Category', verbose_name='カテゴリ')),
            ],
            options={
                'verbose_name': '家計簿',
                'verbose_name_plural': '家計簿',
            },
        ),
    ]