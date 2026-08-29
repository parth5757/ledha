from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, MeView, UserListView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("register/", UserRegisterView := RegisterView.as_view()),
    path("me/", MeView.as_view()),
    path("list/", UserListView.as_view()),
]