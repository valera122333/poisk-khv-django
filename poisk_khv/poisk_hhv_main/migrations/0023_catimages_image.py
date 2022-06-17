# Generated by Django 3.2.9 on 2022-04-26 11:00

from django.db import migrations, models
import django.db.models.deletion
import poisk_hhv_main.models


class Migration(migrations.Migration):

    dependencies = [
        ('poisk_hhv_main', '0022_remove_projects_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок категории')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=poisk_hhv_main.models.upload_gallery_image)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='poisk_hhv_main.catimages')),
            ],
        ),
    ]
