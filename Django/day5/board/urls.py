from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # 로그인 된 사용자만 볼 수 있도록 권한 부여

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),

    path('login/', auth_views.LoginView.as_view(template_name='board/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('signup/', views.signup, name='signup'),
]
