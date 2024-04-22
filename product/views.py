from django.shortcuts import render
from product.models import*
#from marchandi.forms import marchandisePostForm
from django.shortcuts import get_object_or_404

#from product<a href="{% url 'product:post-add' %}">Create a New Post</a>.models import*

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
    product_post = productpost.objects.get(id=post_id)
    data = {
    'post': product_post
    }
    return render(request, 'product/product-post-view.html', data)