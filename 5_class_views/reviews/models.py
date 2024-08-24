from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ReviewModel(models.Model):
    user_name=models.CharField(max_length=100)
    review_text=models.TextField()
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    owner_comment=models.TextField(null=True,blank=True)