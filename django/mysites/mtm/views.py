from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Blog,Author,Entry
import datetime
def testadd(req):
    # b = Blog(name = 'python',tagline = '人生苦短，我用python')
    # b.save()
    #
    #
    # b = Blog.objects.get(id = 1)
    # d = datetime.datetime.now()
    # e = Entry(blog=b,pub_date=d,mod_date=d,n_comments=1)
    # e.save()
    x = Entry.objects.get(id=1)
    name = x.blog.name
    return HttpResponse(name)
