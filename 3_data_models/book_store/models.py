from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}({self.code})"

    class Meta:
        verbose_name_plural="Countries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return f"first_name: {self.first_name} , last_name:{self.last_name}"


class Address(models.Model):
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    author = models.OneToOneField(Author,on_delete=models.CASCADE,null=True)

    
    def __str__(self):
        return f"{self.street, self.postal_code, self.city}"

    class Meta:
        verbose_name_plural = "Address Entries" #changes plural name in Admin


class Book(models.Model):
    # id is automatically added by django
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False,db_index=True)
    published_countries = models.ManyToManyField(Country,related_name="books") #MANY TO MANY!

    def get_absolute_url(self):
        #return reverse("book",args=[self.id]) #using id
        return reverse("book",args=[self.slug])
    
    def __str__(self):
        return f"Title: {self.title},  Author: {self.author} Bestseller: {self.is_bestselling}"
