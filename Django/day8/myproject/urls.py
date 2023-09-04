from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('volt/', include('admin_volt.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]
