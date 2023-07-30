from django.shortcuts import render, redirect
from django.views import generic
from .models import  Video, Comment , CommentFeedback
from django.db.models.aggregates import Count 
from .forms import PostForm
# Create your views here.



def post_list(request):
    data = Video.objects.all()
    return render(request,'videos/index.html',{'videos':data})

def post_detail(request,post_id):
    data = Video.objects.get(id=post_id)
    return render(request,'videos/detail.html',{'videos':data})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/youtube/')
    else:
        form = PostForm()
    
    return render(request,'videos/new.html',{'form':form})

def edit_post(request,post_id):
    data = Video.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/youtube/')
    else:
        form = PostForm(instance=data)
    
    return render(request,'videos/edit.html',{'form':form})


def delet_post(request,post_id):
    data = Video.objects.get(id=post_id)
    data.delete()
    return redirect('/youtube/')
    






    
