from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('getin/', include('google_auth.urls')),
    path('google_workspace_devices/', include('google_workspace_devices.urls')),
    path('', include('google_token.urls')),
]
