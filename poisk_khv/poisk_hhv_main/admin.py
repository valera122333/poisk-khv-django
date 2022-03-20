from django.contrib import admin
from .models import Post, Smi
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'sub_title', 'url']


admin.site.register(Category,  CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
admin.site.site_title = "ПОИСКОВОЕ ДВИЖЕНИЕ РОССИИ"
admin.site.site_header = "ПОИСКОВОЕ ДВИЖЕНИЕ РОССИИ"


# class PoiskAdmin(admin.ModelAdmin):

#     prepopulated_fields = {"slug": ("title",)}
#     fields = (
#         "title",
#         "slug",


#     )


admin.site.register(Post)
admin.site.register(Smi)
