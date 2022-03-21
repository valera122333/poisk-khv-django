from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date
import datetime


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


class OurTeam(models.Model):
    name = CharField(max_length=100,
                     verbose_name="Имя")
    title = CharField(max_length=100, verbose_name="Заголовок")
    Phone = CharField(blank=True,  max_length=100,
                      verbose_name="Номер телефона")

    image = ImageField(upload_to="our_team/images",
                       verbose_name="Изображение")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"


class ActiveTeam(models.Model):
    name = CharField(max_length=100,
                     verbose_name="Имя")
    title = CharField(max_length=100, verbose_name="Заголовок")

    image = ImageField(upload_to="active_team/images",
                       verbose_name="Изображение")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Активная команда "
        verbose_name_plural = "Активная команда"


class AboutUs(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image1 = ImageField(upload_to="about_us/images",
                        verbose_name="Изображение")
    image2 = ImageField(upload_to="about_us/images",
                        verbose_name="Изображение")
    image3 = ImageField(upload_to="about_us/images",
                        verbose_name="Изображение")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "О нас "
        verbose_name_plural = "О нас"


class AboutDocs(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    url = URLField(blank=True, verbose_name="Адрес ссылки")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Документы о нас "
        verbose_name_plural = "Документы о нас"


class AboutPartner(models.Model):
    url = URLField(blank=True, verbose_name="Адрес ссылки")
    image = ImageField(upload_to="about_us/images",
                       verbose_name="Изображение")

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = "Партнеры о нас "
        verbose_name_plural = "Партнеры о нас"


class Projects(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    sub_title = CharField(max_length=100, verbose_name="Подзаголовок")
    summa = CharField(max_length=100, verbose_name="сумма")
    data = CharField(max_length=100, verbose_name="дата")
    description = models.TextField(verbose_name="Описание")
    image1 = ImageField(upload_to="projects/images",
                        verbose_name="Изображение")
    image2 = ImageField(upload_to="projects/images",
                        verbose_name="Изображение")
    image3 = ImageField(upload_to="projects/images",
                        verbose_name="Изображение")
    url = URLField(blank=True, verbose_name="Адрес ссылки")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"


# Здесь переделать
