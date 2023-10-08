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

from django.template.defaultfilters import slugify

# Create your views here.

def index(request):
    # for all user
    limns=limn.objects.all().order_by('id').order_by('?')[:10]
    limn_s=''
    for l in limns:
        
        limn_id=l.id
        username=l.username

        if username=='Anonymous':
          profilepic = 'https://www.seekpng.com/png/small/787-7875841_unknown-magnifying-glass-icon.png'
          name=l.fullname
        else:
            profilepic = userform.objects.get(username=username).profilepic.url
            name = userform.objects.get(username=username).fullname

            
        space_title=l.title
        title=slugify(space_title)
        body=l.body.split()[:20]
        body=' '.join(body)
        limntype=l.limntype
        if l.status=='varified':
            if limntype=='Query':
              append_limn1= '<div  class="card mb-4"><div  class="card-body"><div class="media mb-4">'
              append_limn2= '<img class="d-flex mr-3 rounded-circle" src= "%s' %profilepic+'" style="width:50px !important;height:50px !important;" >'
              
              if username=='Anonymous':
                append_limn3= '<h6> by %s'%name +'(%s)' %username+  '<br><span class="label label-primary">this is a %s'%limntype +  ' &nbsp;limn</span></h6></div>'
              else:
                append_limn3= '<h6> by <a href= "%s">'%username +'%s' %name+  '</a><br><span class="label label-primary">this is a %s'%limntype +  ' &nbsp;limn</span></h6></div>'
              
              append_limn4= '<a  href="thelimn/%s' %limn_id +'/%s" '%title +'> <h5>%s'%space_title+ '</h5></a><hr>'
              append_limn5= '<p class="card-text " >%s' %body +'</p></div><div class="card-footer ">'
              append_limn6= '<a class="btn btn-success" href="thelimn/%s' %limn_id +'/%s" '%title +'>solve it</a>'


              share_limn1='<a class="float-right" href="https://wa.me/?text=https://www.limnstage.com/thelimn/%s' %limn_id +'/%s'%title +'" target="_blank" ><i class="fa fa-whatsapp float-xl-right" style="font-size:36px;color:green"></i></a>'
              share_limn2='<a class="float-right" href="https://www.facebook.com/sharer.php?u=https://www.limnstage.com/thelimn/%s' %limn_id +'/%s'%title +'" target="_blank"><i class="fa fa-facebook-square float-xl-right" style="font-size:36px;color:#3C5A99;"></i></a><h3 class="text-muted float-right">share: </h3></div></div>' 


              limn_new=append_limn1+append_limn2+append_limn3+append_limn4+append_limn5+append_limn6+share_limn1+share_limn2
           
            else:

              append_limn1= '<div  class="card mb-4"><div  class="card-body"><div class="media mb-4">'
              append_limn2= '<img class="d-flex mr-3 rounded-circle" src= "%s' %profilepic+'" style="width:50px !important;height:50px !important;" >'


              if username=='Anonymous':
                    append_limn3= '<h6> by %s'%name +'(%s)' %username+  '<br><span class="label label-primary">this is a %s'%limntype +  ' &nbsp;limn</span></h6></div>'
              else:
                    append_limn3= '<h6> by <a href= "%s">'%username +'%s' %name+  '</a><br><span class="label label-primary">this is a %s'%limntype +  ' &nbsp;limn</span></h6></div>'


              append_limn4= '<a  href="thelimn/%s' %limn_id +'/%s" '%title +'> <h5>%s'%space_title+ '</h5></a><hr>'
              append_limn5= '<p class="card-text " >%s' %body +'</p></div><div class="card-footer ">'
              append_limn6= '<a class="btn btn-primary" href="thelimn/%s' %limn_id +'/%s" '%title +'>read it</a>'


              share_limn1='<a class="float-right" href="https://wa.me/?text=https://www.limnstage.com/thelimn/%s' %limn_id +'/%s'%title +'" target="_blank" ><i class="fa fa-whatsapp float-xl-right" style="font-size:36px;color:green"></i></a>'
              share_limn2='<a class="float-right" href="https://www.facebook.com/sharer.php?u=https://www.limnstage.com/thelimn/%s' %limn_id +'/%s'%title +'" target="_blank"><i class="fa fa-facebook-square float-xl-right" style="font-size:36px;color:#3C5A99;"></i></a><h3 class="text-muted float-right">share: </h3></div></div>' 


              limn_new=append_limn1+append_limn2+append_limn3+append_limn4+append_limn5+append_limn6+share_limn1+share_limn2
            limn_s=limn_s + limn_new

            
    context={
    'limn_post':limn_s,
    }
    return render (request, "index.html", context)


