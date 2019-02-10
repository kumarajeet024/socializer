from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class PostListView(ListView):
     model = Post
     template_name = 'blog/home.html'
     context_object_name = 'posts'
     ordering = ['-date_posted']

class PostDetailView(DetailView):
     model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
     model = Post
     fields = ['title', 'content']
     #code written below add logged in user as an author in the new post created
     #LoginRequiredMixin is used in place of @login required as here we are using class based views
     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)
         #now we return the url of homepage in models


def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title':'About'})
#note:we can not use decorators in class based view and not even the redirect.
