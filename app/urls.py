from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cooking/', views.CookingView.as_view(), name='cooking'),
    path('shop/', views.ShopView.as_view(), name='shop'),
]
