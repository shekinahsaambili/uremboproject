from django.db import models

# Create your models here.
class marchandisePost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
   # photo=models.ImageField(upload_to='photos/')
    price=models.IntegerField(default=0)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)
    def __str__(self):
     return self.title

    def get_absolute_url(self):
        return "/marchandise/post/" + str(self.id) + "/"
