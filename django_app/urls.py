from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
]