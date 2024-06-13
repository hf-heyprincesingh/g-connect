from django.urls import path
from . import views

app_name = "google_workspace_devices"

urlpatterns = [
    path('receive_token/', views.ReceiveTokenView.as_view(), name='receive_token'),
    path("handle_token", views.HandleTokenView.as_view(), name="handle_token"),
]
