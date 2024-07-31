from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_details.models import User, Address
from django.contrib.auth import authenticate, login,logout

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

