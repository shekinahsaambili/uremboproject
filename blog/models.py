from django.db import models
from django.conf import settings

User= settings.AUTH_USER_MODEL

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class BlogPost(models.Model):
    class Meta:
        permissions = [
        ("publish_blogpost", "Can publish a BlogPost")
        ]
   # author= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)
    # Create your models here.
    def __str__(self):
     return self.title

    def get_absolute_url(self):
        return "/blog/post/" + str(self.id) + "/"

    