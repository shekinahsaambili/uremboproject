from django.shortcuts import render

def index(request):
    return render(request,'pages/index.html')


def account(request):
    return render(request,'pages/account.html')

def apropos(request):
    return render(request, 'pages/apropos.html')

# Create your views here.
