from rest_framework_simplejwt.views import TokenObtainPairView

from birthday_reminder.accounts.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
