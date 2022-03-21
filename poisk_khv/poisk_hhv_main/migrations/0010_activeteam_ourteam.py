# Generated by Django 3.2.9 on 2022-03-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0009_auto_20220320_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=100, verbose_name='Имя')),
                ('title', models.CharField(default=True, max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='active_team/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Активная команда ',
                'verbose_name_plural': 'Активная команда',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=100, verbose_name='Имя')),
                ('title', models.CharField(default=True, max_length=100, verbose_name='Заголовок')),
                ('Phone', models.CharField(blank=True, default=True, max_length=100, verbose_name='Номер телефона')),
                ('image', models.ImageField(upload_to='our_team/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
    ]
