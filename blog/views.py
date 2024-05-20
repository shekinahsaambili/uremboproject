from django.shortcuts import render, redirect
from django.http import Http404
from blog.models import*
from blog.forms import  salonform, productform
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required,login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group

#   from .models import blog_post


def home(request):
    posts = (salon.objects
    .filter(is_published=True)
    .order_by('-pub_date')[:10]
    )
 
    data = {
    'saloons': posts
    }
    return render(request, 'blog/home.html', data)

def home_prod(request):
    produits = product.objects.all()
    data = {
    'poste': produits
    }
    return render(request, 'blog/product.html', data) 

def salon_view(request, post_id):
    saloon = salon.objects.get(id=post_id)
    
    data = {
    'post': saloon
    }
    return render(request, 'blog/salon_view.html', data)

def product_view(request, post_id):
    produit = product.objects.get(id=post_id)
    
    data = {
    'poste': produit
    }
    return render(request, 'blog/product_view.html', data)

def salon_detail(request, post_id):
    print(list(sal.id for sal in salon.objects.all()))
    saloon = get_object_or_404(salon, id=post_id) 
    data = {
    'post': saloon
    }
    return render(request, 'blog/salon_detail.html', data)

def product_detail(request, product_id):
    produit = get_object_or_404(product, id=product_id) 
    data = {
        'produit': produit
    }
    return render(request, 'blog/product_detail.html', data)


@login_required
@permission_required('blog:add_salon', raise_exception=True)
def add_salon(request):
    if request.method == "POST":
        form = salonform(request.POST, request.FILES)
        if form.is_valid():
            saloon = form.save()
            return redirect(saloon)  
    else:
        form = salonform()
    return render(request, 'blog/add_salon.html', { 'form': form })

@login_required
@permission_required('blog:add_product', raise_exception=True)
def add_product(request):
    if request.method == "POST":
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(product)  
    else:
        form = productform()
    return render(request, 'blog/product_add.html', { 'form': form })


@permission_required('blog.change_salon', raise_exception=True)
def changer_salon(request, post_id):
    saloon = get_object_or_404(salon, id=post_id)
    if request.method == 'POST':
        form = salonform(request.POST, request.FILES, instance=saloon) 
        if form.is_valid():
            saloon = form.save()   
            return redirect('/blog/')
    else:
        form = salonform(instance=saloon)
    return render(request, 'blog/changer_salon.html', { 'form': form, 'post': saloon })

@permission_required('blog.delete_salon', raise_exception=True)
def delete_salon(request, post_id):
 post = get_object_or_404(salon, id=post_id)
 if request.method == "POST":
    post.delete()
    return redirect('/blog/')
 return render(request, 'blog/delete_salon.html', { 'post': post })

from datetime import datetime 
def blog_post_publish(request, post_id):
 post = get_object_or_404(salon, id=post_id)
 if request.method == "POST":
    post.is_published = True
    post.pub_date = datetime.now()
    post.save()
 
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



