from django.db import models
from django.contrib import admin
class Products(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductID=models.IntegerField(primary_key=True)
    Category=models.CharField(max_length=20)
    Brand=models.CharField(max_length=30)
    Price=models.IntegerField()
    Rating=models.IntegerField()
    Review=models.CharField(max_length=100)
class ProductsAdmin(admin.ModelAdmin):
    list_display=["ProductName","ProductID","Category","Brand","Price","Rating","Review"]    


