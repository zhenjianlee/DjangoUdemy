from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    author = models.one_to_one_field(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street, self.postal_code, self.city}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return f"first_name: {self.first_name} , last_name:{self.last_name}"

class Book(models.Model):
    # id is automatically added by django
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False,db_index=True)

    def get_absolute_url(self):
        #return reverse("book",args=[self.id]) #using id
        return reverse("book",args=[self.slug])
    
    def __str__(self):
        return f"Title: {self.title},  Author: {self.author} Bestseller: {self.is_bestselling}"
