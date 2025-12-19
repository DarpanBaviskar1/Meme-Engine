from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('memes/', views.memes_view, name='memes_view'),
    path('generate-meme/', views.generate_meme_view, name='generate_meme'),
    path('meme-generator/', views.meme_generator_view, name='meme_generator'),
    path('generate-meme2/', views.generate_meme2_view, name='generate_meme2'),
]