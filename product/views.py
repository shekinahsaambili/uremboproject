from django.shortcuts import render

from blog.models import*

def home(request):
    posts = (productpost.objects
    .filter(is_published=True)
    .order_by('-pub_date')[:10]
    )
 # only published posts
    # We pass the set of posts to the template
    data = {
    'blog_posts': posts
    }
    return render(request, 'product/home.html', data)

def product_post_view(request, post_id):
    blo_post = productpost.objects.get(id=post_id)
    data = {
    'post': blog_post
    }
    return render(request, 'product/product-post-view.html', data)