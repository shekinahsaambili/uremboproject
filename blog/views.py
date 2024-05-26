from django.shortcuts import render, redirect
from django.http import Http404
from blog.models import*
from blog.forms import  salonform, productform, RatingForm
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

# def home_evaluation(request):
#     evaluation = salonEvaluation.objects.all()
#     data = {
#     'evaluation':  evaluation
#     }
#     return render(request, 'blog/evaluations_commentaire.html', data) 

def home_evaluation(request, post_id):
    saloon = get_object_or_404(salon, id=post_id)
    evaluation = salonEvaluation.objects.filter(salon_de_coiffure=saloon)
    data = {
        'evaluation': evaluation
    }
    return render(request, 'blog/evaluations_commentaire.html', data)

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
   # print(list(sal.id for sal in salon.objects.all()))
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

def product_partage(request, product_id):
    product = Product.objects.get(id=product_id)
    share_data = {
        'title': product.nom_produit,
        'url': request.build_absolute_uri(product.get_absolute_url()),
        'image': request.build_absolute_uri(product.photos.url) if product.photos else '',
        'description': product.description,
    }
    return render(request, 'product_detail.html', {'product': product, 'share_data': share_data})



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
def saloon_publish(request, post_id):
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

def search_produit(request):
    if 'search' in request.GET:
        produit = request.GET['search']
        produits = product.objects.filter(nom_produit__icontains=produit)
    else:
        produits = product.objects.all()
    
    context = {
        'poste': produits
    }
    
    return render(request, 'blog/product.html', context)

def search_salon(request):
    if 'search' in request.GET:
        saloon = request.GET['search']
        salons = salon.objects.filter(nom_salon__icontains=saloon)
    else:
        salons = salon.objects.all()
    
    data = {
        'saloons': salons
    }
    
    return render(request, 'blog/home.html', data)



@login_required
def evaluer_salon(request, post_id):
    post = get_object_or_404(salon, id=post_id)
    user = request.user

    if request.method == 'POST':
        form = RatingForm(request.POST, request.FILES)
        if form.is_valid():
            rating_data = form.cleaned_data

            # ici on essaie de verifier si une évaluation existe déjà pour cet utilisateur et ce salon
            existing_rating = salonEvaluation.objects.filter(utilisateur=user, salon_de_coiffure=post).first()

            if existing_rating:
                # si oui, nous mettons à jour l'évaluation existante
                existing_rating.etoiles = rating_data['etoiles']
                existing_rating.commentaire = rating_data['commentaire']
                existing_rating.save()
            else:
                # ici sinon on crée une nouvelle évaluation 
                new_rating = salonEvaluation.objects.create(
                    utilisateur=user,
                    salon_de_coiffure=post,
                    etoiles=rating_data['etoiles'], 
                    commentaire=rating_data['commentaire']
                )

            return redirect('blog:post_view', post_id=post.id)
    else:
        form = RatingForm()

    # ici on recupere tous les commentaires donnés par l'utilisateur pour ce salon de coiffure
    user_ratings = salonEvaluation.objects.filter(utilisateur=user, salon_de_coiffure=post)

    return render(request, 'blog/evaluer_salon.html', {'form': form, 'post': post, 'user_ratings': user_ratings})


def liste_salons(request):
    salons = salon.objects.all()
    nombre_salons = len(salons)

    data = {
        'nombre_salons': nombre_salons
    }

    return render(request, 'blog/home.html', data)

@login_required
def ajouter_favoris(request, post_id):
    user = request.user
    saloon = salon.objects.get(id=post_id)

    try:
        favoris = Favoris.objects.get(user=user, saloon=saloon)
        favoris.delete()  # Retirer de favoris
    except Favoris.DoesNotExist:
        Favoris.objects.create(user=user, saloon=saloon)  # Ajouter aux favoris

    return redirect('blog:post_view', post_id=post_id)