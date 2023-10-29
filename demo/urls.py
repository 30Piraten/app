from django.urls import path
from .views import DemoViews, DemoPageView, DemoFormView

urlpatterns = [
    path("post/new", DemoFormView.as_view(), name="new_post"),
    path("post/<int:pk>/", DemoPageView.as_view(), name="post_detail"),
    path("", DemoViews.as_view(), name="home"),
]
