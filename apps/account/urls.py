from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

app_name = 'account'
urlpatterns = [
    # url(r'^$', views.HomePage, name='home_page'),
    path('auth', include('djoser.urls')),
    path('auth', include('djoser.urls.authtoken')),
]
