from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path('specific/', views.specific, name='specific'),
    path('article/<int:article_id>', views.article, name='article'),
    path('search', views.search, name="search")
]