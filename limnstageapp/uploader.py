from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from .models import userform, limn, limnanswer, files
import re
from itertools import chain





def uploader(request):
  if 'username' in request.COOKIES and 'thepass' in request.COOKIES:
      username = request.COOKIES['username']
      if request.method=="POST" and request.FILES['file']:
          images=request.FILES['file']
          filedata=files.objects.create(
                  username=username,
                  images=images
                  )
      images=files.objects.filter(username=username) .order_by('-id')
      context={
      'images':images
      }  
      return render (request, "uploader.html", context)
  else:
    return HttpResponse('you cannot upload picture because you are anonymous.. Sorry for this. But you can put you image url or link in url field near browse server button ')
