from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    GENDER_CHOICES=[
        ('M', 'MEN'),
        ('W', 'WOMEN')
    ]
    name = models.CharField(max_length=255,)
    image = models.ImageField(upload_to='category_image/',blank=False, null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XS', 'Extra Small'),
        ('XS', 'Extra Small'),
    ]
    COLOR_CHOICES = [
        ('reb', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  unique=True)
    image = models.ImageField(upload_to='Product/',blank=False, null=False)
    brand = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    rating = models.FloatField(default=0.0)
    buy_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class meta:
        unique_together = ('user', 'product')

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class meta:
        unique_together = ('user', 'product')