from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Address
# from user_details.models import User 

from django.contrib.auth import authenticate, login,logout

# Create your views here.


# Create your views here.
def patients_signup_view(request):
    context={}
    if request.method=='POST':
        
        print('--------',request.POST)
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        line1=request.POST.get('line1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        profile=request.FILES.get('profile')
        
        user_type='patient'
        if email !="":
            if  not User.objects.filter(email__iexact=email).exists():
            # return render(request,'patients_register.html',context)
                if pass1 != "" and pass2 !="":
                    if pass1 == pass2:
                        user=User.objects.create(first_name=fname,last_name=lname,username=uname,email=email,user_type=user_type,profile=profile)
                        add=Address.objects.create(line1=line1,city=city,state=state,pincode=pincode,user=user)                    
                        user.set_password(pass1)
                        user.save()
                        login(request,user)
                        return redirect('patient_dashboard', id=user.id)
                    else:
                        print('---pass not match')
                        context['message']="password did'nt match"
                else:
                    print('---pass not null')
                    context['message']="password field cannot be null"
            else:
                    # print('---pass not null')
                    context['message']="Email alreay exists"
        else:
            print('---emil not null')
            context['message']="email field cannot be null"
        return render(request,'patients_register.html',context)
    # context['message']="email field cannot be null"
    return render(request,'patients_register.html',context)







def Doc_signup_view(request):
    context={}
    if request.method=='POST':
        
        print('--------',request.POST)
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        line1=request.POST.get('line1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        profile=request.FILES.get('profile')
        

        user_type='doctor'
        if email !="":
            if  not User.objects.filter(email__iexact=email).exists():
            # return render(request,'patients_register.html',context)
                if pass1 != "" and pass2 !="":
                    if pass1 == pass2:
                        user=User.objects.create(first_name=fname,last_name=lname,username=uname,email=email,user_type=user_type,profile=profile)
                        add=Address.objects.create(line1=line1,city=city,state=state,pincode=pincode,user=user)   

                        user.set_password(pass1)
                        user.save()
                        login(request,user)
                        return redirect('doctor_dashboard', id=user.id)
                    else:
                        print('---pass not match')
                        context['message']="password did'nt match"
                else:
                    print('---pass not null')
                    context['message']="password field cannot be null"
            else:
                   
                    context['message']="Email alreay exists"
        else:
            print('---emil not null')
            context['message']="email field cannot be null"
        return render(request,'doctors_register.html',context)    

    return render(request,'doctors_register.html',context)





def login_page(request):
    context={}
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.filter(email__iexact=email)
        if user.exists():
            user=user.last()
            if user.check_password(password):
                login(request,user)
                if user.user_type=='PATIENT' or user.user_type=='patient':
                    return redirect('patient_dashboard', id=user.id)
                else:
                    return redirect('doctor_dashboard', id=user.id )
            else:
                print('---Incorrect')
                context['message']="Incorrect Password"
        else:
            print('---not exist')
            context['message']="Email does not exist"
        return render(request,'login.html',context)    
    return render(request,'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')