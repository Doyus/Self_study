from django.db import models

# Create your models here.
class User_info(models.Model):
    name = models.CharField(max_length=20)
    pwd=models.IntegerField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    sex=models.CharField(max_length=2)
    class Meta:
        db_table = 'user_table'
class Adimn_info(models.Model):
    name = models.CharField(max_length=20)
    pwd=models.IntegerField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    sex=models.CharField(max_length=2)
    class Meta:
        db_table = 'admin_table'