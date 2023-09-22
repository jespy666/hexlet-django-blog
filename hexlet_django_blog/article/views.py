from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'article/articles.html',
            context={'articles': articles}
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'article/create.html',
            context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно создана')
            return redirect('articles')
        else:
            messages.error(
                request,
                'Произошла ошибка при добавлении статьи'
            )
        return render(
            request,
            'article/create.html',
            context={'form': form}
        )
