from django.contrib import admin
from hexlet_django_blog.article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('timestamp', admin.DateFieldListFilter),)
