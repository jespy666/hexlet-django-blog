from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path(
        '<int:id>/edit/',
        ArticleFormEditView.as_view(),
        name='article_update'
    ),
    path(
        '<int:id>/delete/',
        ArticleFormDeleteView.as_view(),
        name='article_delete'
    ),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='article_create'),
]
