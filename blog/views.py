from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

'''posts = [

    {
        'author': 'NinjaKai',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '29 Jan 2019'
    },
    {
    'author': 'NinjaKai407',
    'title': 'Blog Post 2',
    'content': 'Second Post Content',
    'date_posted': '30 Jan 2019'
    }
]'''

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    #for templates
    context = {
        #'posts':posts      #contect helps us to post data on templates nd its also third argument or render
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title':'About'})
