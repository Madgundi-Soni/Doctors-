from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_details.models import User, Address


def Doctor_dashboard(request,id):
    context={}
    user=User.objects.get(id=id)
    add=Address.objects.filter(user=user).last()
    print('------addd',add)
    context['user']=user
    context['add']=add
    return render(request,'doctor/doctor_dashboard.html',context)

def logout_view(request):
    logout(request)
    return redirect('login_page')

