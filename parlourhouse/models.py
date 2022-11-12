from django.db import models

# Create your models here.

    
class parlourhouse(models.Model):
    parlourhouse_address =models.CharField(max_length=50,default="")
    parlourhouse_name =models.CharField(max_length=50,default="")
    parlour_city =models.CharField(max_length=50,default="")     
    
    def __str__(self):
        return self.parlourhouse_address
