from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.db import models

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.id

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_code = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    quantity = models.CharField(max_length=13)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    author = models.JSONField(max_length=500)
    book_details = models.CharField(max_length=1000, null=True, blank=True)
    book_image = models.ImageField(upload_to='files', blank=True, null=True)

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# class Book_Image(models.Model):
#     id = models.AutoField(primary_key=True)
#     book_code = models.ForeignKey(Book, related_name="Book_Image", on_delete=models.DO_NOTHING)
#     book_image = models.ImageField(upload_to='upload_to', blank=True, null=True)


    def __str__(self):
        return self.id

