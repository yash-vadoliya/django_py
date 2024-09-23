from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('about', views.about, name='about'),
]
