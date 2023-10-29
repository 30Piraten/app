from django.urls import path
from .views import DemoViews, DemoPageView

urlpatterns = [
    path("post/<int:pk>/", DemoPageView.as_view(), name="post_detail"),
    path("", DemoViews.as_view(), name="home"),
]
