from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:list_by_category', args=[self.slug])

class Product(models.Model):
    METAL_CHOICES = [
        ('GD', 'Gold'),
        ('DM', 'Diamond'),
        ('PT', 'Platinum'),
        ('SL', 'Silver'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    metal_type = models.CharField(max_length=2, choices=METAL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    karat = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id, self.slug])
