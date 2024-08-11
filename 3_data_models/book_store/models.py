from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    # id is automatically added by django
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False,db_index=True)

    def get_absolute_url(self):
        #return reverse("book",args=[self.id]) #using id
        return reverse("book",args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Book =>Title: {self.title}, Rating: {self.rating} Author: {self.author} Bestseller: {self.is_bestselling}"
