"""URL configuration for birthday_reminder project."""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from birthday_reminder.accounts.views import MyTokenObtainPairView

apipatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("birthday/", include("birthday_reminder.birthdays.urls")),
]

urlpatterns = [
    path("api/", include(apipatterns)),
]
