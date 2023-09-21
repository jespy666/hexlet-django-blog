from django.urls import path
from .views import IndexView, ArticleView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view(), name='article')
]
