from django.contrib import admin
from .models import user_contact

class contatdata(admin.ModelAdmin):
    list_display=['name','email','mobile']


admin.site.register(user_contact,contatdata)




