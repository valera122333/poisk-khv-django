# Generated by Django 3.2.9 on 2022-03-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0011_auto_20220321_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='image1',
            field=models.ImageField(upload_to='about_us1/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image2',
            field=models.ImageField(upload_to='about_us2/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image3',
            field=models.ImageField(upload_to='about_us3/images', verbose_name='Изображение'),
        ),
    ]
