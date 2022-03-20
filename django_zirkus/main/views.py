from django.shortcuts import render
from .models import Post
from .forms import PostForm



# Create your views here.
def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'main/index.html', context)

