from django.shortcuts import render

# Create your views here.

#This is plural checklist


from django.shortcuts import render
from .models import Post
from pdapp.forms import PostForm

def home(request):
    form=PostForm()
    return render(request,'home.html',{'form':form})
