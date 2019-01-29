from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [

    {
        'author': 'NinjaKai'
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': '29 Jan 2019'
    },
    {
    'author': 'NinjaKai407'
    'title': 'blog post 2',
    'content': 'second post content',
    'date_posted': '30 Jan 2019'
    }
]

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    #for templates
    return render(request, 'blog/home.html')
def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html')
all participants must be from the affiliated institues og akyu
