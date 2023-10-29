from django.urls import path
from .views import UserSignUpView

url_patterns = [
    path("signup/", UserSignUpView.as_view(), name="signup"),
]
