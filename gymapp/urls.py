from django.contrib import admin
from django.urls import path,include
from gymapp import views

urlpatterns = [ 
    path('',views.index),
    path('contact/',views.contact),
    path('trainer/',views.trainer),
    path('why/',views.why),
]
