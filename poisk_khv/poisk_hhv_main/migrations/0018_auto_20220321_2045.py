# Generated by Django 3.2.9 on 2022-03-21 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0017_auto_20220321_1946'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
