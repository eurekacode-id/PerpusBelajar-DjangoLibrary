from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=10)
    author = models.CharField(max_length=50)
    cover = models.ImageField(default='no_image_found.jpg', blank=True)

    def __str__(self):
        return self.title





# command for making migrations
# py manage.py makemigrations
# py manage.py migrate