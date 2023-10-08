from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from .models import userform, limn, limnanswer, files
from django.core.paginator import Paginator
import re
from itertools import chain
from django.contrib.auth.models import User

def unsolved(request):  # for unsolved queries 
   u = User.objects.all()
   print(u)
   limntype='Query'
   recent=limn.objects.filter(limntype=limntype).order_by('-id')[:25]
   context={
            'recent':recent,
   }
   return render (request, "unsolved-queries.html", context)

def recentarticle(request):  # for stories articles
   limntype='Story/Article'
   recent=limn.objects.filter(limntype=limntype).order_by('-id')[:25]
   context={
            'recent':recent,
   }
   return render (request, "recent-articles.html", context)
