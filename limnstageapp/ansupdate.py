from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from .models import userform, limn, limnanswer, files, limnanswer
import re
from itertools import chain
from django.http import Http404


def ansupdate(request, title, id):  # for limning something 
   if request.method=="POST":
      new_answers=request.POST.get("editor1")
      edit_ans =limnanswer.objects.get(id=id)
      edit_ans.answer=new_answers
      edit_ans.save()
      title=limn.objects.get(id=edit_ans.limnid).title
      new_title=title.replace(" ", "-")
      return redirect('../../thelimn/%s' %edit_ans.limnid+ '/%s' %new_title  )

   update_ans=get_object_or_404(limnanswer, id=id) 
   limn_id=update_ans.limnid
   all_limns = get_object_or_404(limn, id=limn_id)
   limner_username=all_limns.username
#   pic=userform.objects.get(username=limner_username).profilepic.url
   context={
   "update_ans":update_ans,
   "limns":all_limns
     }
   return render (request, "ansupdate.html", context)

