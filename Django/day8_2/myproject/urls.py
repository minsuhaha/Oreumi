from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# swagger 문서를 위한 패키지
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

schema_view = get_schema_view(
    openapi.Info(
        title = 'DRF TEST API',
        default_version = 'v1.0',
        description = 'DRF 생애 최초는 아니지만 테스트해보기',
        terms_of_service = 'https://127.0.0.1/terms/',
        contact = openapi.Contact(email= "haminsu5@gmail.com"),
        license = openapi.License(name = 'MIT'), # MIT -> 모두가 쓸 수 있는
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include('admin_black.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('drf_test.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
