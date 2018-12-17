from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('admin', views.addnew, name='addnew'),
    path('login', views.login, name='login'),
    path('film.html/<int:film_id>/', views.filmpage, name='listpage'),
]