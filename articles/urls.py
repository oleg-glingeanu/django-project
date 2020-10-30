from django.urls import path

from . import index

from .views import (
    ArticleListView,
    ArticleUpdateView, # new
    ArticleDetailView, # new
    ArticleDeleteView, # new
    ArticleCreateView, # new
)

urlpatterns=[
    path('<int:pk>/edit/',
        ArticleUpdateView.as_view(), name='article_edit'), # new
     path('<int:pk>/',
        ArticleDetailView.as_view(), name='article_detail'), # new
     path('<int:pk>/delete/',
        ArticleDeleteView.as_view(), name='article_delete'), # new
    path('events/', index.events, name='events_page'),
    path('news/', index.news, name='news_page'),
    path('covid/', index.covid, name='covid_page'),
    path('new/', ArticleCreateView.as_view(), name='article_new'), # new
    path('', ArticleListView.as_view(), name='article_list'),
]