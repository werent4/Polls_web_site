from django.urls import path

from . import views
#API
app_name = 'API'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('weather/', views.weather, name= 'weather')
]
