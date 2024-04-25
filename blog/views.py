from django.shortcuts import render, redirect
from django.http import Http404
from blog.models import*
from blog.forms import BlogPostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required,login_required

#   from .models import blog_post


def home(request):
    posts = (BlogPost.objects
    .filter(is_published=True)
    .order_by('-pub_date')[:10]
    )
 # only published posts
    # We pass the set of posts to the template
    data = {
    'blog_posts': posts
    }
    return render(request, 'blog/home.html', data)

def blog_post_view(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)
    data = {
    'post': blog_post
    }
    return render(request, 'blog/blog-post-view.html', data)

def blog_post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id) 
    data = {
    'post': blog_post
    }
    return render(request, 'blog/blog-post-detail.html', data)

@login_required
@permission_required('blog:add_blogpost', raise_exception=True)
def blog_post_add(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect(blog_post)  # redirects to blog_post.get_absolute_url()
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog-post-add.html', { 'form': form })

@permission_required('blog.change_blogpost', raise_exception=True)
def blog_post_change(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id) # Need to fetch the specific object
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            blog_post = form.save()   # This will update the object
            return redirect('/blog/')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blog-post-change.html', { 'form': form, 'post': post })

@permission_required('blog.delete_blogpost', raise_exception=True)
def blog_post_delete(request, post_id):
 post = get_object_or_404(BlogPost, id=post_id)
 if request.method == "POST":
    post.delete()
    return redirect('/blog/')
 return render(request, 'blog/blog-post-delete.html', { 'post': post })

from datetime import datetime 
def blog_post_publish(request, post_id):
 post = get_object_or_404(BlogPost, id=post_id)
 if request.method == "POST":
    post.is_published = True
    post.pub_date = datetime.now()
    post.save()
 # Redirect to the post's detail page
 return redirect(post)

 # Liste des chemins d'accès des images
IMAGES = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
]

def random_image_view(request):
    # Choisir aléatoirement une image
    random_image = random.choice(IMAGES)
    context = {
        "random_image": random_image
    }
    return render(request, "home.html", context)