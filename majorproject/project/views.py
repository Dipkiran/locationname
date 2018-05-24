
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
#upload display page
def index(request):
    return render(request,"index.html")
