from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class DemoViews(ListView):
    model = Post
    template_name = "home.html"


class DemoPageView(DetailView):
    model = Post
    template_name = "post_detail.html"
