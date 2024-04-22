from django.shortcuts import render, redirect

from marchandise.models import*
from marchandise.forms import marchandisePostForm
from django.shortcuts import get_object_or_404
#from .models import marchandise_post


def home(request):
    posts = (marchandisePost.objects
    .filter(is_published=True)
    .order_by('-pub_date')[:10]
    )
 # only published posts
    # We pass the set of posts to the template
    data = {
    'marchandise_posts': posts
    }
    return render(request, 'marchandise/home.html', data)

def marchandise_post_view(request, post_id):
    marchandise_post = marchandisePost.objects.get(id=post_id)
    data = {
    'post': marchandise_post
    }
    return render(request, 'marchandise/marchandise_post.html', data)
def march_post_detail(request, post_id):
    marchandise_post = get_object_or_404(BlogPost, id=post_id) 
    data = {
    'post':marchandise_post
    }
    return render(request, 'marchandise/marchandise-post-detail.html', data)

def march_post_add(request):
    if request.method == "POST":
        form = marchandisePostForm(request.POST)
        if form.is_valid():
            marchandise_post = form.save()
            return redirect(marchandise_post)  
    else:
        form = marchandisePostForm()
    return render(request, 'marchandise/marchandise-post-add.html', { 'form': form })


def march_post_change(request, post_id):
    post = get_object_or_404(marchandisePost, id=post_id) # Need to fetch the specific object
    if request.method == "POST":
        form = marchandiseForm(request.POST, instance=post)
        if form.is_valid():
            marchandise_post = form.save()   # This will update the object
            return redirect('/marchandise/')
    else:
        form = marchandiseForm(instance=post)
    return render(request, 'marchandise/marchandise-post-change.html', { 'form': form, 'post': post })

def march_post_delete(request, post_id):
 post = get_object_or_404(marchandisePost, id=post_id)
 if request.method == "POST":
    post.delete()
    return redirect('/marchandise/')
 return render(request, 'marchandise/marchandise-post-delete.html', { 'post': post })

from datetime import datetime 
def march_post_publish(request, post_id):
 post = get_object_or_404(marchandisePost, id=post_id)
 if request.method == "POST":
    post.is_published = True
    post.pub_date = datetime.now()
    post.save()
 # Redirect to the post's detail page
 return redirect(post)