from django.shortcuts import render

posts = [
    {
        'date': '01-01-01',
        'title': 'GODT NYT JO!',
        'content': 'Zirkusrevsbech er online og kører afsted med 240 i timen.\nEn hel masse tekst her. Den er lang og det er spændende. Totalt langt tekstoverflow, pow pow!'
    },
    {
        'date': '20-02-22',
        'title': 'Anden post',
        'content': 'Også pænt lang tekst der.'
    },
]




# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context)

