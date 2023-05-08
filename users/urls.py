# from django.urls import path, include
# from .views import UserLoginView, SignupView, UserLogoutView
#
# from . import views
#
# app_name = 'users'
#
# urlpatterns = [
#     path('',views.index, name= 'index'),
#     path('account/', views.account, name= 'account'),
#     path(r'login/', UserLoginView.as_view(), name= 'login'),
#     path(r'logout/', UserLogoutView.as_view(), name= 'logout'),
#     #path(r'singup/', SignupView.as_view(), name= 'singup'),
#     path(r'signup/', SignupView.as_view(), name= 'signup'),
#     path('google-auth/', include('social_django.urls', namespace='social')),
# ]


from django.urls import path, include
from .views import UserLoginView, SignupView, UserLogoutView

from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index, name= 'index'),
    path('account/', views.account, name= 'account'),
    path(r'login/', UserLoginView.as_view(), name= 'login'),
    path(r'logout/', UserLogoutView.as_view(), name= 'logout'),
    path(r'singup/', SignupView.as_view(), name= 'singup'),
    #path('google-auth/', include('social_django.urls', namespace='social')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]