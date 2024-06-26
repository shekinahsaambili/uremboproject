from django.db import models

class productpost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    #image= models.ImageField()
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
      return self.title

# Create your models here.
