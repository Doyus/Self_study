from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_comments = models.IntegerField()
