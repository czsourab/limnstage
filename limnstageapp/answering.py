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
from limnstageapp.views import captcha
from django.template.defaultfilters import slugify


def answering(request, title, id):  # for limning something 
   if request.method=="POST":
      if captcha(request) ==True:
          answer=request.POST.get("editor1")
          username = 'Anonymous'
          fullname = request.POST.get("fullname")
          no_space_title=title.replace("-", " ")
          status='unvarified'
          exists=limnanswer.objects.filter(answer=answer)
          if exists.count() >=1:
             ansexists='yes'
          else:
            ansdata=limnanswer.objects.create( 
              username=username, 
              title=no_space_title, 
              fullname=fullname,
              limnid=id,
              status=status, 
              answer=answer
              )
            return redirect('thelimn', id=ansdata.limnid, title=slugify(ansdata.title))
      else:
         all_limns=get_object_or_404(limn, id=id)
         no_cha='no_cha'
         context={
          "no_cha":no_cha,
          "limns":all_limns
        }
         return render (request, "answering.html", context) 


   all_limns=get_object_or_404(limn, id=id)
#   pic=userform.objects.get(username=limner_username).profilepic.url
   context={
   "limns":all_limns
     }
   return render (request, "answering.html", context)

