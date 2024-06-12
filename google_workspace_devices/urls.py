from django.urls import path
from . import views

app_name = "google_workspace_devices"
urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view), 
]
