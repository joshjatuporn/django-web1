from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm
from django.db.models import Q
# Create your views here.

def index(request):
#    return HttpResponse("Hello, Django ja")
# Table.objects.method()
# Query all posts
     all_posts = Post.objects.all()
     #name = "Josh"
     #return render(request, 'blog/index.html', {'all_posts':all_posts, 'name':name})
     return render(request, 'blog/home.html', {'all_posts':all_posts})
     # {'key': value}

def single_post(request, id):
     #quiry
     single_post = Post.objects.get(pk = id)
     return render(request, 'blog/single-post.html', {'single_post': single_post})

def contact(request):
     # check the incoming method
     if request.method == "POST":
          # print("Okay this is POST")
          form = ContactForm(request.POST)
          if form.is_valid():
               # save into DB
               form.save()
               # Redirect to home page
               return redirect('/')
     else:
          # print("This is GET")
          form = ContactForm()

     return render(request, 'blog/contact.html', {'form': form})





# 10.01am
def search(request):
     search_post = request.GET.get('q')
     
     if search_post:
          # print('Okay')
          posts = Post.objects.filter(Q(title__icontains=search_post))
     else:
          return redirect('/')
     return render(request, 'blog/search.html', {'posts':posts})
    #return render(request, 'blog/search.html', {'posts':posts})