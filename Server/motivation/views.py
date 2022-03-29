from django.shortcuts import render
from motivation.models import Post

# Create your views here.

def Posts(request, title):
    post = Post.objects.get(title = title)
    context = {'post':post}
    return render(request,'post.html')