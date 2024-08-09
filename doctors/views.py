from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from user_details.models import *
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view






def Doctor_dashboard(request,id):
    context={}
    user=User.objects.get(id=id)
    add=Address.objects.filter(user=user).last()
    
    print('------username',user.first_name)
    context['user']=user
    context['add']=add
    return render(request,'doctor/doctor_dashboard.html',context)

# @api_view(('GET',))
def blogs(request):
    context={}
    # blog=Blogs.objects.filter(user_id=request.user.id)
    # cat=Categories.objects.all()
    # context['blog']=blog
    # context['cat']=cat
    if request.GET.get('cat'):
        cat = request.GET.get('cat')
        context['blog']=Blogs.objects.filter(user_id=request.user.id,categories_id=cat).order_by('-id')    
    else:
        context['blog']=Blogs.objects.filter(user_id=request.user.id).order_by('-id')    
    context['cat']=Categories.objects.filter()
    

   
    return render(request,'doctor/blogs.html',context)

# @api_view(('POST',))
from django.http import JsonResponse
def blog_submit(request ):
    if request.method=='POST':
        # print('==============post',request.body)
        print('==============postfile',request.FILES)
        print('==============post',request.POST)
        title=request.POST.get('title')
        category=request.POST.get('category')
        summary=request.POST.get('summary')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        if request.POST.get('draft'):
            is_draft=request.POST.get('draft')
            if is_draft=="True":
                is_draft=True
        else:
            is_draft=False

        data=Blogs.objects.create(title=title,image=image,summary=summary,content=content,categories_id=category,user=request.user,is_draft=is_draft)
        data.save()

        return  JsonResponse({'msg': 'done' }, status=201)
    return  JsonResponse({'msg': 'not found' }, status=404)



def Edit_blog(request,id):
    context={}
    context['blog']=Blogs.objects.get(id=id)
    context['cat']=Categories.objects.filter()
    if request.method=="POST":
        title=request.POST.get('title')
        category=request.POST.get('category')
        summary=request.POST.get('summary')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        if request.POST.get('draft'):
            is_draft=request.POST.get('draft')
            if is_draft=="True":
                is_draft=True
        else:
            is_draft=False
        blog=Blogs.objects.get(id=id)
        blog.title=title
        blog.categories.id=category
        blog.summary=summary
        blog.content=content
        if image:
            blog.image=image
        blog.save()
        return  JsonResponse({'msg': 'done' }, status=201)
    # return  JsonResponse({'msg': 'not found' }, status=404)
    return render(request,'doctor/edit_blog.html',context)


def logout_view(request):
    logout(request)
    return redirect('login_page')

