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

def thelimn(request, title, id):
    # logged in user
    if 'username' in request.COOKIES and 'thepass' in request.COOKIES:
        username = request.COOKIES['username']
        thepass = request.COOKIES['thepass']
        match1 = userform.objects.filter(username=username)
        match2 = userform.objects.filter(password=thepass)
          
        if match1.count()==1 and match1.count()==1:
          loggeduser = userform.objects.filter(username=username)
        
       # posting answer
        if request.method=='POST':
          answer=request.POST.get("editor1")
          username = request.COOKIES['username']
          no_space_title=title.replace("-", " ")
          status='unvarified'
          exists=limnanswer.objects.filter(answer=answer)
          if exists.count() >=1:
            ansexists='yes'
            context={
            'ansexists':ansexists,
            }
            return render (request, "thelimn.html", context)
          else:
            userdata=limnanswer.objects.create( 
              username=username, 
              title=no_space_title, 
              limnid=id,
              status=status, 
              answer=answer
              )
          ansexists=''

       # content FETCH USING ID
        limns = limn.objects.filter(id=id)
        
        if limns.count()==0:
          raise Http404("page does not exist")
        else:
          for l in limns:
            l_user=l.username
            no_space=l.title.replace(" ", "-")
            tagslist=l.subjects.split(',') 
          tag_related=''
          for t in tagslist:
              collect_related=[]
              new_tag_related=''
              new_tag_related1=limn.objects.filter(
                Q(subjects__icontains=t)
                ).exclude(id=id).order_by('-id')[:30]
              collect_related=list(chain(new_tag_related1, new_tag_related))
              tag_related=list(chain(tag_related, collect_related))
          tag_related=reversed(list(set(tag_related)))
          tag_related=(list(chain(tag_related)))

          if l_user=='Anonymous':
            pic='https://www.seekpng.com/png/small/787-7875841_unknown-magnifying-glass-icon.png'
          else:
            pic=userform.objects.get(username=l_user).profilepic.url

          post_related=[]
          related=tag_related
          #load answer
          get_answer=limnanswer.objects.filter(limnid=id)[:10]
          theanswer=''
          for a in get_answer:
            ans_username=a.username
            ans_id=a.id

            ans_fullname=a.fullname
            if ans_username== 'Anonymous':
              ans_pic='https://www.seekpng.com/png/small/787-7875841_unknown-magnifying-glass-icon.png'
              fullname=ans_fullname
            else:
              fullname=userform.objects.get(username=ans_username).fullname
              ans_pic=userform.objects.get(username=ans_username).profilepic.url

            answer=a.answer
            if username==a.username:
               new_answer='<div class="author-info"><img class="propic" src="%s '%ans_pic+'"    ><h6><a href= "../../%s" '%ans_username+'>%s'%fullname+'(%s)'%ans_username+'</a><span class="text-muted"> answered %s'%ans_id+'</span> </h6></div><a href="../../ansupdate/%s'%ans_id+'/%s'%title+'" class="float-right text-danger">Edit</a><hr>%s'%answer+'<hr>'
               theanswer=theanswer + new_answer
            else:
               new_answer='<div class="author-info"><img class="propic" src="%s '%ans_pic+'"    ><h6><a href= "../../%s" '%ans_username+'>%s'%fullname+'(%s)'%ans_username+'</a><span class="text-muted"> answered %s'%ans_id+'</span> </h6></div><hr>%s'%answer+'<hr>'
               theanswer=theanswer + new_answer
          # send to template
          for l in limns:
            tagslist=l.subjects.split(',')
          Query='Query'
          Anonymous='Anonymous'
          context={
            'loggeduser':loggeduser,
            'limns':limns,
            'pic':pic,
            'related':related,
            'Query':Query,
            'theanswer':theanswer,
            'tagslist':tagslist,
            'Anonymous': Anonymous
            }   
          return render (request, "thelimn.html", context)

     # all user can see 
    limns = limn.objects.filter(id=id)

      #ALL USER CAN ANSWER:
    if request.method=='POST':
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
            userdata=limnanswer.objects.create( 
              username=username, 
              title=no_space_title, 
              fullname=fullname,
              limnid=id,
              status=status, 
              answer=answer
              )
            ansexists=''
          no_cha=''
      else:
        no_cha='no_cha'
    else:
      no_cha=''


    if limns.count()==0:
          raise Http404("page does not exist")
    else:
      for l in limns:
        l_user=l.username
        no_space=l.title.replace(" ", "-")
        tagslist=l.subjects.split(',')
         #tags in html for the template view


        #related post   
  
      tag_related=''
      for t in tagslist:
          new_tag_related=''
          new_tag_related1=limn.objects.filter(
            Q(subjects__icontains=t)
            ).exclude(id=id).order_by('-id')[:30]
          tag_related3=list(chain(new_tag_related, new_tag_related1))
      tag_related=reversed(list(set(tag_related3)))
      tag_related=(list(chain(tag_related)))
      

      #anonymous pic
      if l_user=='Anonymous':
        pic='https://www.seekpng.com/png/small/787-7875841_unknown-magnifying-glass-icon.png'
      else:
        pic=userform.objects.get(username=l_user).profilepic.url

     
      related=tag_related


      get_answer=limnanswer.objects.filter(limnid=id).order_by('-id')
      theanswer=''
      Query='Query'
      Anonymous='Anonymous'
      for a in get_answer:
        ans_username=a.username
        ans_fullname=a.fullname
        answer=a.answer
        ans_id=a.id
        #differentiate anonymous answer
        if ans_username== 'Anonymous':
          ans_pic='https://www.seekpng.com/png/small/787-7875841_unknown-magnifying-glass-icon.png'
          fullname=ans_fullname
          new_answer='<div class="imp-link-answer">%s'%fullname+'(%s)'%ans_username+' answered %s'%ans_id+' </div>%s'%answer+''

        else:
          fullname=userform.objects.get(username=ans_username).fullname
          ans_pic=userform.objects.get(username=ans_username).profilepic.url
          new_answer='<div class="imp-link-answer"><a href= "../../%s" '%ans_username+'>%s'%fullname+'(%s)'%ans_username+'</a> answered %s'%ans_id+'</div>%s'%answer+''

        
        
        theanswer=theanswer + new_answer
      context={
          'theanswer':theanswer,
          'limns':limns,
          'pic':pic,
          'Query':Query,
          'related':related,
          'tagslist':tagslist,
          'Anonymous':Anonymous,
          'no_cha':no_cha
        }
      return render (request, "thelimn.html", context) 

