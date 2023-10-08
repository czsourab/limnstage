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

def limnvarification(request):  # for unsolved queries 
   u = User.objects.all()
   print(u)
   status='unvarified'
   unvarified=limn.objects.filter(status=status).order_by('-id')[:25]
   context={
            'unvarified':unvarified,
   }
   return render (request, "varification-limns.html", context)

