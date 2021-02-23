from django.contrib import admin
from .models import *

admin.site.register(GalleryCategory)
admin.site.register(GalleryPost)
admin.site.register(ArticleCategory)


class ArticleContentAdmin(admin.StackedInline):
    model = ArticleContent

@admin.register(ArticleContent)
class ArticleAdmin(admin.ModelAdmin):
    pass

class ArticleImagesAdmin(admin.StackedInline):
    model = ArticleImages

@admin.register(ArticleImages)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleContentAdmin, ArticleImagesAdmin]

    class Meta:
        model = Article