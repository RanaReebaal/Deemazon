from django.db import models

# Create your models here.

class jewelleryhouse(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    quailty = models.CharField(max_length=64)
    images = models.ImageField(upload_to = "images" ,default="")
    def __str__(self):
        return self.brand

