from django.shortcuts import render
from .models import Post, Details
from .forms import PostForm



# Create your views here.
def home(request):

    posts = []
    cards = []
    details = Details.objects.first()

    postsobjects = Post.objects.all()

    for obj in postsobjects:
        if "Kort" in obj.admin_name:
            cards.append(obj)
        elif "Post" in obj.admin_name:
            posts.append(obj)
    

    context = {
        'posts': posts,
        'cards': cards,
        'details': details
    }

    return render(request, 'main/index.html', context)

