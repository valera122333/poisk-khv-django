from email.policy import default
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
        verbose_name = "Документы отделения"
        verbose_name_plural = "Документы отделения"


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


def upload_gallery_image(instance, filename):
    return f"images/CatImages/{instance.category.title}/gallery/{filename}"


class CatImages(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок категории")
    description = CharField(
        max_length=200, verbose_name="Описание", default='')
    image1 = models.ImageField(upload_to='cat/images', default='')
    audio_file = models.FileField(
        default='', verbose_name='песенка', upload_to="audio_player/")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


class Image(models.Model):

    image = models.ImageField(upload_to=upload_gallery_image)
    category = models.ForeignKey(
        CatImages, on_delete=models.CASCADE, related_name="images")


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description1 = models.TextField(
        verbose_name="Описание1", blank=True, null=True)
    image1 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение1", null=True, blank=True)

    description2 = models.TextField(
        verbose_name="Описание2", null=True, blank=True)
    image2 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение2", null=True, blank=True)

    description3 = models.TextField(
        verbose_name="Описание3", null=True, blank=True)
    image3 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение3", null=True, blank=True)

    description4 = models.TextField(
        verbose_name="Описание4", null=True, blank=True)
    image4 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение4", null=True, blank=True)

    description5 = models.TextField(
        verbose_name="Описание5", null=True, blank=True)
    image5 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение5", null=True, blank=True)

    description6 = models.TextField(
        verbose_name="Описание6", null=True, blank=True)
    image6 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение6", null=True, blank=True)

    description7 = models.TextField(
        verbose_name="Описание7", null=True, blank=True)
    image7 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение7", null=True, blank=True)

    description8 = models.TextField(
        verbose_name="Описание8", null=True, blank=True)
    image8 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение8", null=True, blank=True)

    description9 = models.TextField(
        verbose_name="Описание9", null=True, blank=True)
    image9 = models.ImageField(upload_to="article/images",
                               verbose_name="Изображение9", null=True, blank=True)

    description10 = models.TextField(
        verbose_name="Описание10", null=True, blank=True)
    image10 = models.ImageField(upload_to="article/images",
                                verbose_name="Изображение10", null=True, blank=True)

    date = models.DateField(default=datetime.date.today, verbose_name="Дата")

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name = "Статья"
        verbose_name_plural = "Статья"
