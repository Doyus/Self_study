from django.db import models

# Create your models here.
class A_class(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

class B_class(models.Model):
    ac = models.ForeignKey(A_class,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

class G_class(models.Model):
    bc = models.ForeignKey(A_class,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=100)
