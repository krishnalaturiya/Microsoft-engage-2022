from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from flask import redirect

# 
def home(request):
    return render(request,"home.html")


    

