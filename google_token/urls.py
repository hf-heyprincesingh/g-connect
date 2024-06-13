from django.urls import path
from google_token.views import GoogleTokenView

urlpatterns = [
    path("getGoogleToken", GoogleTokenView.as_view(), name="google_token"),
]
