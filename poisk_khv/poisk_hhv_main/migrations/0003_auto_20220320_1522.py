# Generated by Django 3.2.9 on 2022-03-20 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0002_remove_news_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='blog/images', verbose_name='Изображение')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
