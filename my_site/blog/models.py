from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name}, {self.last_name} , {self.email}"

    class Meta:
        pass

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="posts")
    title= models.CharField(max_length=200)
    excerpt=models.CharField(max_length=200)
    image_name=models.CharField(max_length=200)
    date=models.DateField()
    slug=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return f"{self.title} , {self.excerpt} , {self.date}"

    class Meta:
        pass


class Tag(models.Model):
    posts=models.ManyToManyField(Post,related_name="posts")
    caption=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

    class Meta:
        pass
