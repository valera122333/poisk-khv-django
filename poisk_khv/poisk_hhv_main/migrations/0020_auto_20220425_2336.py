# Generated by Django 3.2.9 on 2022-04-25 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0019_book_group_books'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Group_books',
        ),
    ]
