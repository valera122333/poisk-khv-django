from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date
import datetime

# class News(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Заголовок")
#     slug = models.SlugField(
#         max_length=255, unique=True, db_index=True, verbose_name="URL"
#     )
#     content = models.TextField(blank=True, verbose_name="Текст статьи")
#     photo = models.ImageField(
#         upload_to="news/images", verbose_name="Фото")
#     time_create = models.DateTimeField(
#         auto_now_add=True, verbose_name="Время создания")
#     time_update = models.DateTimeField(
#         auto_now=True, verbose_name="Время изменения")
#     # is_published = models.BooleanField(default=True, verbose_name="Публикация")

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('new_detail', kwargs={'new_slug': self.slug})

#     class Meta:
#         verbose_name = "Новости"
#         verbose_name_plural = "Новости"
#         ordering = ["time_create", "title"]


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="blog/images",
                              verbose_name="Изображение")
    date = models.DateField(default=datetime.date.today, verbose_name="Дата")

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Smi(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")

    image = ImageField(upload_to="smi_about/images",
                       verbose_name="Изображение")
    url = URLField(blank=True, verbose_name="Адрес ссылки")
    date = DateField(default=date.today, verbose_name="Дата")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Сми о нас"
        verbose_name_plural = "Сми о нас"


class Article(models.Model):
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, verbose_name='категория')
    title = CharField(default=True, max_length=100, verbose_name="Заголовок")
    sub_title = CharField(default=True, max_length=100,
                          verbose_name="Подзаголовок")
    url = URLField(blank=True, verbose_name="Адрес ссылки")

    class Meta:
        verbose_name = "Статья реестра"
        verbose_name_plural = "Статья реестра"


class Category(models.Model):
    atricles = models.ForeignKey(
        Article, default=True, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=64, verbose_name='название категории')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория реестра статьи"
        verbose_name_plural = "Категория реестра статьи"
