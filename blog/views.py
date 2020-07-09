from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs':blogs})

def blog_post(request, blog_id):
    #blog_obj = Blog.objects.get(id=blog_id)
    blog_obj = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_post.html', {'blog_obj':blog_obj})
