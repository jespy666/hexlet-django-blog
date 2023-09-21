from django.urls import path
from .views import IndexView

urlpatterns = [
    path(
        'articles/',
        IndexView.as_view(),
        name='articles'
    ),
]
