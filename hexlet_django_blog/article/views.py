from django.shortcuts import render
from django.views import View
from .models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles.html',
            context={'articles': articles}
        )
