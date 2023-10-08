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


def privacy(request):  # for privacy policy 
   return render (request, "privacy-policy.html")
def contact(request):  # for contact us form 
   return render (request, "contact-us.html")

