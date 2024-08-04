from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_details.models import User, Address
from django.contrib.auth import authenticate, login,logout
from doctors.models import Blogs,Categories


def Patient_dashboard(request,id):
    context={}
    user=User.objects.get(id=id)
    add=Address.objects.filter(user=user).last()
    print('------addd',add)
    context['user']=user
    context['add']=add
    return render(request,'patient/patient_dashboard.html',context)

def logout_view(request):
    logout(request)
    return redirect('login_page')


def Blogs_list(request):
    context={}
    if request.GET.get('cat'):
        cat = request.GET.get('cat')
        context['blogs']=Blogs.objects.filter(is_draft=False,categories_id=cat).order_by('-id')    
    else:
        context['blogs']=Blogs.objects.filter(is_draft=False).order_by('-id')    
    context['cat']=Categories.objects.filter()
    
    return render(request,'patient/patient_blogs.html',context)