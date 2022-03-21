# Generated by Django 3.2.9 on 2022-03-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0010_activeteam_ourteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image1', models.ImageField(upload_to='about_us/images', verbose_name='Изображение')),
                ('image2', models.ImageField(upload_to='about_us/images', verbose_name='Изображение')),
                ('image3', models.ImageField(upload_to='about_us/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'О нас ',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.AlterField(
            model_name='activeteam',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='activeteam',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='Phone',
            field=models.CharField(blank=True, max_length=100, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
