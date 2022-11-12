from django.db import models

# Create your models here.

class fashionhouse(models.Model):
    fashion_name = models.CharField(max_length=50)
    fashionhouse_address = models.CharField(max_length=50)
    about_fashionhouse = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.fashion_name


