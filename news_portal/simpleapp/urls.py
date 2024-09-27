from django.urls import path
from .views import (
    NewsListView,
    NewsDetailView,
    NewsCreateView,
    ArticleCreateView,
    NewsUpdateView,
    ArticleUpdateView,
    NewsDeleteView,
    ArticleDeleteView,
    SearchView
)

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('news/search/', SearchView.as_view(), name='news_search'),
]
