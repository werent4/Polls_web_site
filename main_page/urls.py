from django.urls import path

from . import views

app_name = 'main_page'
urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name= 'about_us')
]