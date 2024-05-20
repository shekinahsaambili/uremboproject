from django.contrib import admin

# Register your models here.
from .models import *
# register each model with the admin site
admin.site.register(salon)
admin.site.register(product)