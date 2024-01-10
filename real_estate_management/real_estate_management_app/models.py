from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TenantDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    address = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=13)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    proof =  models.ImageField(upload_to='images')
    status = models.CharField(max_length=10)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.fname


class PropertyDetails(models.Model):
    pname = models.CharField(max_length=100,unique=True)
    address = models.EmailField(max_length=100)
    locaton = models.CharField(max_length=130)
    features = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.pname


class UnitDetails(models.Model):
    properti = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    uname = models.EmailField(max_length=100)
    rent_cost = models.CharField(max_length=13)
    types = models.CharField(max_length=500)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.types



class RentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    address = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=13)
    properti = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    paddress = models.EmailField(max_length=100)
    locaton = models.CharField(max_length=130)
    features = models.CharField(max_length=500)
    unit = models.ForeignKey(UnitDetails, on_delete=models.CASCADE)
    uname = models.EmailField(max_length=100)
    rent_cost = models.CharField(max_length=13)
    types = models.CharField(max_length=500)
    enddate = models.CharField(max_length=500)
    rentdate = models.CharField(max_length=500)
    status = models.CharField(max_length=10)
    
        
        