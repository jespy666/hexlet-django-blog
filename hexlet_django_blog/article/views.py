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


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            'article/update.html',
            context={'form': form, 'article_id': article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно изменена')
            return redirect('articles')
        else:
            messages.error(request, 'Ошибка при редактировании статьи')
        return render(
            request,
            'article/update.html',
            context={'form': form, 'article_id': article_id}
        )

