from django.urls import path
from .views import (
    DemoViews, DemoPageView, DemoFormView, DemoUpdateView, DemoDeleteView
)

urlpatterns = [
    path("post/<int:pk>/delete", DemoDeleteView.as_view(), name="delete_post"),
    path("post/<int:pk>/edit/", DemoUpdateView.as_view(), name="edit_post"),
    path("post/new", DemoFormView.as_view(), name="new_post"),
    path("post/<int:pk>/", DemoPageView.as_view(), name="post_detail"),
    path("", DemoViews.as_view(), name="home"),
]
