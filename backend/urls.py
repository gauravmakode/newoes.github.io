from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from .views import validate_jwt_token
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),

    path('user/', include('user.urls')),
    path('sheet/', include('sheet.urls')),
    path('testpaper/', include('testpaper.urls')),

    path('validate/', validate_jwt_token),
    path('login/', obtain_jwt_token),

    path('verify/', verify_jwt_token),
    path('refresh/', refresh_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
