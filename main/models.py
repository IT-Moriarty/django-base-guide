from encodings.punycode import T
from itertools import product
from os import name
from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,unique=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    decription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avaliable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

