from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from .models import userform, limn, limnanswer, files, asked
import re
from itertools import chain
from django.http import Http404
from limnstageapp.views import captcha


def profile(request, name):
    # ask to user
    if request.method=="POST":
        return postinglimn(request, name)
    

    details = userform.objects.filter(username=name)
    if details.count()==0:
        raise Http404("This user does not exist")
    else:
        #theusername = request.COOKIES['username']
        total_limns=limn.objects.filter(username=name).count()
        limns=limn.objects.filter(username=name).order_by('-id')[:10]
        extra=limn.objects.all().order_by('?')[:3]
        context={
            'details':details,
            'total_limns':total_limns,
            'limn':limns,
            'extra':extra
        }
        return render (request, "profile.html", context)

 # solved by profile user
def solved(request, name):

    details = userform.objects.filter(username=name)
    if details.count()==0:
        raise Http404("This user does not exist")
    else:
        #theusername = request.COOKIES['username']
        total_limns=limn.objects.filter(username=name).count()
        limns=limn.objects.filter(username=name).order_by('-id')[:10]
        extra=limn.objects.all().order_by('?')[:3]
        context={
            'details':details,
            'total_limns':total_limns,
            'limn':limns,
            'extra':extra
        }
        return render (request, "profile.html", context)
    

# asked by profile user
def askedbypeople(request, name):
    if request.method=="POST":
        return postinglimn(request, name)
    
    details = userform.objects.filter(username=name)
    if details.count()==0:
        raise Http404("This user does not exist")
    else:
        
        allaskedlimn=asked.objects.filter(askeduser=name)[:10]
        limns = asked.objects.none()
        for akl in allaskedlimn:
            req_id=akl.limnid
            reqlimn=limn.objects.filter(id=req_id).order_by('-id')
            limns = limns | reqlimn


        total_limns=limn.objects.filter(username=name).count()
        extra=limn.objects.all().order_by('?')[:3]
        context={
            'details':details,
            'total_limns':total_limns,
            'limn':limns,
            'extra':extra
        }

        return render (request, "profile.html", context)




def postinglimn(request, name):
    
    # for authorized uer who wants to post
            if 'username' in request.COOKIES and 'thepass' in request.COOKIES:
                username = request.COOKIES['username']
                fullname = userform.objects.get(username=username).fullname
                limntype=request.POST.get("limn_type")
                title=request.POST.get("title")
                body=request.POST.get("editor1")
                tag=request.POST.get("subjects")
                status='unvarified'
                exists=limn.objects.filter(title=title).count()
                if exists >=1:
                    details = userform.objects.filter(username=name)
                    total_limns=limn.objects.filter(username=name).count()
                    limns=limn.objects.filter(username=name).order_by('-id')[:10]
                    extra=limn.objects.all().order_by('?')[:3]
                    exsist_limn='yes'
                    loggeduser='loggeduser'
                    context={
                        'details':details,
                        'total_limns':total_limns,
                        'limn':limns,
                        'extra':extra,
                        'exsist_limn':exsist_limn,
                        'loggeduser':loggeduser
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
                    askdata=asked.objects.create(
                            askeduser=name,
                            limnid=limndata.id
                            )    
                    return redirect('thelimn', id=limndata.id, title=limndata.title.replace(" " , "-")) 
            
            # for annonymous user
            else :
                  
                username = 'Anonymous'
                fullname = request.POST.get("fullname")
                limntype=request.POST.get("limn_type")
                title=request.POST.get("title")
                body=request.POST.get("editor1")
                tag=request.POST.get("subjects")
                status='unvarified'
                # calling the captcha function from views.py file
                if captcha(request) ==True:  

                    exists=limn.objects.filter(title=title).count()
        
                    if exists >=1:
                        details = userform.objects.filter(username=name)
                        total_limns=limn.objects.filter(username=name).count()
                        limns=limn.objects.filter(username=name).order_by('-id')[:10]
                        extra=limn.objects.all().order_by('?')[:3]
                        exsist_limn='yes'
                        context={
                            'details':details,
                            'total_limns':total_limns,
                            'limn':limns,
                            'extra':extra,
                            'exsist_limn':exsist_limn
                        }
                        return render( request, 'profile.html', context) 
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
                        askdata=asked.objects.create(
                                askeduser=name,
                                limnid=limndata.id
                                ) 
                        return redirect('thelimn', id=limndata.id, title=limndata.title.replace(" " , "-")) 
                else:
                    details = userform.objects.filter(username=name)
                    total_limns=limn.objects.filter(username=name).count()
                    limns=limn.objects.filter(username=name).order_by('-id')[:10]
                    extra=limn.objects.all().order_by('?')[:3]
                    exsist_limn='yes'
                    no_cha='no_cha'
                    context={
                        'details':details,
                        'total_limns':total_limns,
                        'limn':limns,
                        'no_cha':no_cha
                    }
                    return render( request, 'profile.html', context) 
    