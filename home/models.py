from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

   


class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)
    core = models.CharField(max_length=50)

    

class Book(models.Model):
    category= models.ForeignKey(Category,  on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)



