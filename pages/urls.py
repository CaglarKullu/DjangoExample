from django.urls import path
from pages import views


urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('contact', views.contact),
]
