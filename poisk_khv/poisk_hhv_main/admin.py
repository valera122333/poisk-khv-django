from django.contrib import admin
from .models import AboutDocs, AboutUs, ActiveTeam,  OurTeam, Post, Projects, Smi, Image, CatImages, Article


# Register your models here.
admin.site.site_title = "ПОИСКОВОЕ ДВИЖЕНИЕ РОССИИ"
admin.site.site_header = "ПОИСКОВОЕ ДВИЖЕНИЕ РОССИИ"


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(CatImages)
class ArtistAdmin(admin.ModelAdmin):

    inlines = [ImageInline, ]


admin.site.register(Article)
admin.site.register(Projects)

admin.site.register(AboutDocs)
admin.site.register(AboutUs)
admin.site.register(OurTeam)
admin.site.register(ActiveTeam)
admin.site.register(Post)
admin.site.register(Smi)
