from django.urls import path
from . import views

urlpatterns = [
    path('social_login/', views.social_login_view, name='social_login'),
    path('main/', views.login_success, name='main'),
    path('logout/', views.logout_view, name='logout'),
]
