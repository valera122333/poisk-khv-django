# Generated by Django 3.2.9 on 2022-06-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0027_auto_20220611_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='catimages',
            name='description',
            field=models.CharField(default='', max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catimages',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок категории'),
        ),
    ]