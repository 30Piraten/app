from django.urls import path
from .views import DemoViews

urlpatterns = [
    path("", DemoViews.as_view(), name="home"),
]
