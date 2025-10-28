from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cooking/', views.CookingView.as_view(), name='cooking'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('video/', views.VideoView.as_view(), name='video'),
    path('google51925de0612ccd11.html/', views.google_search_console, name='google_search_console'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
]
