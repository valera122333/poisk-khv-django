# Generated by Django 3.2.9 on 2022-03-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0015_aboutdocs'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, verbose_name='Адрес ссылки')),
                ('image', models.ImageField(upload_to='about_us/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Документы о нас ',
                'verbose_name_plural': 'Документы о нас',
            },
        ),
    ]
