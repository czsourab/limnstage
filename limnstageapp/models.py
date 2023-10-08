from django.db import models
import re
from django.utils.timezone import now
from django.shortcuts import render, HttpResponse, get_object_or_404,redirect, reverse
from django.template.defaultfilters import slugify

# Create your models here.
class userform(models.Model):
    username = models.CharField(max_length=30)
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    profilepic = models.FileField(upload_to='profilepics', blank=True)
    def __str__(self):
       return self.username
    def get_user_profile(self):
        return 'profile/%s' %self.username

class limn(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    title=models.CharField(max_length=500)
    body=models.TextField(blank=True)
    limntype=models.CharField(max_length=30)
    subjects= models.CharField(max_length=200, blank=True, null=True)
    status= models.CharField(max_length=10, blank=True, null=True)
    date=models.DateTimeField(default=now, null=True)

    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse("thelimn", kwargs={"id": self.pk, "title": slugify(self.title)})
    
    

class limnanswer(models.Model):
    username=models.CharField(max_length=30)
    title=models.CharField(max_length=500)
    answer=models.TextField()
    limnid=models.IntegerField()
    fullname=models.CharField(max_length=50, blank=True, null=True)
    status= models.CharField(max_length=10, blank=True, null=True)
    date=models.DateTimeField(default=now, null=True)

    def __str__(self):
       return self.title

class files(models.Model):
    username=models.CharField(max_length=30)
    images = models.FileField(upload_to='limnpics', blank=True)

    def __str__(self):
        return self.username

class asked(models.Model):
    askeduser=models.CharField(max_length=30)
    limnid=models.IntegerField()

    def __str__(self):
        return self.askeduser