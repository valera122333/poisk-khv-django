# Generated by Django 3.2.9 on 2022-04-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0020_auto_20220425_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
