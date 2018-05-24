from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *
#model admin options
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","mainlocation","othername",]
    #list_display_links = ["updated"]


    class Meta:
        model = tree
admin.site.register(tree, PostModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","location","death",]
    #list_display_links = ["updated"]


    class Meta:
        model = information
admin.site.register(information, PostModelAdmin)
