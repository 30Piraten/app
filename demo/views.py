from django.views.generic import ListView
from .models import Post

# Create your views here.


class DemoViews(ListView):
    model = Post
    template_name = "home.html"
