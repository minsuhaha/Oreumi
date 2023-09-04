from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/' , include('users.urls')),
    path('', include('social_django.urls', namespace='social')),
    
    path('accounts/', include('allauth.urls')),
]
