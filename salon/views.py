from django.shortcuts import render
from salon.models import*

def home(request):
    posts = (salon.objects
        .filter(is_published=True)
        .order_by('-pub_date')[:10]
     ) # only published posts
    # We pass the set of posts to the template
    data = {
    'blog_posts': posts
    }
    return render(request, 'salon/home.html', data)


def salon_post_view(request, post_id):
    blog_post = salon.objects.get(id=post_id)
    
    data = {
    'post': blog_post
    }
    return render(request, 'salon/salon_post.html', data)