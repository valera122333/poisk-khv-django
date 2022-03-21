from django.contrib import admin
from .models import AboutDocs, AboutPartner, AboutUs, ActiveTeam,  OurTeam, Post, Projects, Smi


# Register your models here.
admin.site.site_title = "ПОИСКОВОЕ ДВИЖЕНИЕ РОССИИ"
admin.site.site_header = "ПОИСКОВОЕ ДВИЖЕНИЕ РОССИИ"


admin.site.register(Projects)
admin.site.register(AboutPartner)
admin.site.register(AboutDocs)
admin.site.register(AboutUs)
admin.site.register(OurTeam)
admin.site.register(ActiveTeam)
admin.site.register(Post)
admin.site.register(Smi)
