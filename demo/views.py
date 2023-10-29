from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.


class DemoViews(ListView):
    model = Post
    template_name = "home.html"


class DemoPageView(DetailView):
    model = Post
    template_name = "post_details.html"


class DemoFormView(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ["title", "author", "body"]
