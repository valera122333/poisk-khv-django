# Generated by Django 3.2.9 on 2022-06-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0030_alter_catimages_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catimages',
            name='audio_file',
            field=models.FileField(default='', upload_to='audio_player/', verbose_name='песенка'),
        ),
    ]
