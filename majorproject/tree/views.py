from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
#upload display page
from .models import *
from .forms import *


#upload display page
def index(request):

    queryset_list = tree.objects.all()
    form = LocationForm(request.POST or None)
    location = request.POST.get('location')
    death = request.POST.get('death')

    if form.is_valid():
        for qs in queryset_list:
            if location in qs.othername:
                location = qs.mainlocation
                places = information(location= location, death= death)
                places.save()

    context={
        "form":form,
        "queryset_list":queryset_list,
    }
    return render(request, 'index.html',context)
