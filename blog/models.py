from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)
    # Create your models here.
    def __str__(self):
     return self.title