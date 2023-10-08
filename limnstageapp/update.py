from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from .models import userform, limn, limnanswer, files
import re
from itertools import chain
from django.http import Http404


def update(request, title, id):  # for limning something 
  if request.method=="POST":
        new_limntype=request.POST.get("limn_type")
        new_title=request.POST.get("title")
        new_body=request.POST.get("editor1")
        new_tag=request.POST.get("subjects")
        edit_limn = limn.objects.get(id=id)
        edit_limn.title =new_title
        edit_limn.limntype =new_limntype
        edit_limn.body=new_body
        edit_limn.subjects=new_tag
        edit_limn.save()
        username=limn.objects.get(id=id).username
        return redirect('../../%s' %username)

           

  if 'username' in request.COOKIES and 'thepass' in request.COOKIES:    
        updatelimn=get_object_or_404(limn, id=id) 
        username = request.COOKIES['username']
        thepass = request.COOKIES['thepass']
        if username==updatelimn.username:
            match1 = userform.objects.filter(username=username)
            match2 = userform.objects.filter(password=thepass)
            if match1.count()==1 and match1.count()==1:
                  loggeduser = userform.objects.filter(username=username)
                  context={
                  "loggeduser":loggeduser,
                  "updatelimn":updatelimn
                  }
                  return render (request, "update.html", context)
            else:
              return HttpResponse("You are not authorized of this limn")      
        else:
              return HttpResponse("You are not authorized of this limn")
