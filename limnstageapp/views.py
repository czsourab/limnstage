import requests #pip install requests
import json

from django.conf import settings
from django.contrib import messages

from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from .models import userform, limn, limnanswer, files
import re
from itertools import chain
from django.contrib.sitemaps import Sitemap
from django.template.defaultfilters import slugify

# Create your views here.

def adstxt(request):
     return render(request, "ads.txt")

def signup(request):
    # if 'signup' in request.POST:
    #   print('signup')
    # if 'fillup' in request.POST:
    #   print('fillup')
    # del request.session['name']
    if request.method == "POST":
        uploaded_file=request.FILES['profilepic']
        username=request.POST.get("username")
        fullname=request.POST.get("fullname")
        email=request.POST.get("email")
        password=request.POST.get("password")  
        # request.session['name'] = username                
        pass1=pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=23)
        match = userform.objects.filter(username=username)
        match = userform.objects.filter(email=email)
        if match.count()>0:
           error="username exixts"
           context={
            "error":error
          }
           return render(request, "signup.html", context)
        else:
            # Unable to find a user, this is fine
          userdata=userform.objects.create(
          username=username,
          fullname=fullname,
          email=email,
          password=pass1,
          profilepic=uploaded_file
          )
          return redirect('index')
    return render(request, "signup.html")






def login(request):
    if request.method=="POST":
      username=request.POST.get("username")
      password=request.POST.get("password")
      match = userform.objects.filter(username=username)
      if match.count()==0:
        error='error'
        context={
          "error":error
        }


        return render (request, "login.html", context)
      else:
        thepass = userform.objects.get(username=username).password
        verify=pbkdf2_sha256.verify(password, thepass)
        if verify==True:
          response = render(request, "home.html") 
          response.set_cookie('username', username, max_age=2592000)
          response.set_cookie('thepass', thepass, max_age=2592000)
          return response
        else:
          error='error'
          context={
            "error":error
            }
          return render (request, "login.html", context)
    return render (request, "login.html")













def limning(request):  # for limning something 

  
  if request.method=="POST":
    # for authorized uer who wants to post
    if 'username' in request.COOKIES and 'thepass' in request.COOKIES:
        username = request.COOKIES['username']
        fullname = userform.objects.get(username=username).fullname
        limntype=request.POST.get("limn_type")
        title=request.POST.get("title")

        title=" ".join(title.split())

        body=request.POST.get("editor1")
        tag=request.POST.get("subjects")
        status='unvarified'
        exists=limn.objects.filter(title=title).count()
        if exists >=1:
          exsist_limn='yes'
          context={
            'exsist_limn':exsist_limn
          }
          return render( request, 'limning.html', context)
        else:
          limndata=limn.objects.create(
                fullname=fullname,
                title=title,
                body=body,
                limntype=limntype,
                username=username,
                subjects=tag,
                status=status
                )    
          return redirect('thelimn', id=limndata.id, title=slugify(limndata.title))


       # for annonymous user
    else :
        username = 'Anonymous'
        if captcha(request) ==True:
          fullname = request.POST.get("fullname")
          limntype=request.POST.get("limn_type")
          title=request.POST.get("title")

          title=" ".join(title.split())

          body=request.POST.get("editor1")
          tag=request.POST.get("subjects")
          status='unvarified'
          exists=limn.objects.filter(title=title).count()
          if exists >=1:
            exsist_limn='yes'
            context={
              'exsist_limn':exsist_limn
            }
            return render( request, 'limning.html', context)
          else:
            limndata=limn.objects.create(
                  fullname=fullname,
                  title=title,
                  body=body,
                  limntype=limntype,
                  username=username,
                  subjects=tag,
                  status=status
                  )    
            
            return redirect('thelimn', id=limndata.id, title=slugify(limndata.title))
        else:
          print('no')
          no_cha='no_cha'
          context={
            "no_cha":no_cha
          }
          return render ( request, "limning.html", context)
   # checking the logged in user      

  if 'username' in request.COOKIES and 'thepass' in request.COOKIES:
      username = request.COOKIES['username']
      thepass = request.COOKIES['thepass']
      match1 = userform.objects.filter(username=username)
      match2 = userform.objects.filter(password=thepass)
      if match1.count()==1 and match1.count()==1:
        loggeduser = userform.objects.filter(username=username)
        context={
          "loggeduser":loggeduser
        }
        return render (request, "limning.html", context)
  else:
     return render (request, "limning.html")


 

 #captcha matcing
def captcha(request):


            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': '6Le00nwUAAAAAEy-szHGzK1l4xqLVpMR0wre7YOW',
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                return True
            else:
                return False
            

    












    #sitemap
class limnSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = "https"

    def items(self):
        return limn.objects.filter(status='varified')

    def lastmod(self, obj):
        return obj.date
