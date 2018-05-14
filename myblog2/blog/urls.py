from . import views
from django.contrib import admin
from django.urls import path

urlpatterns=[
    path('', views.LatestArticle.as_view(), name = 'home'),
    path('articles', views.ArticleListView.as_view(), name = 'articles'),
    path('videotut', views.VideoTutListView.as_view(), name = 'videos'),
    path('stories', views.StoriesListView.as_view(), name = 'stori'),
    path('codes', views.CodeListView.as_view(), name = 'code'),
    path('poetry', views.PoetryListView.as_view(), name = 'poet'),
    path('projects', views.ProjectsListView.as_view(), name = 'proj'),
    path('chords', views.GuitarListView.as_view(), name = 'guitar'),
    path('blogtut', views.BlogTutorialListView.as_view(), name = 'blogtut'),
    path('aboutme', views.About.as_view(), name = 'about'),
]