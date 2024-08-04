from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/<int:id>/',views.Doctor_dashboard,name='doctor_dashboard'),   
    path('logout_view/',views.logout_view,name='logout_view'),   
    path('blog_submit/',views.blog_submit,name='blog_submit'),   
    path('blogs/',views.blogs,name='blogs'),   
    path('edit_blog/<int:id>/',views.Edit_blog,name='edit_blog'),   
    

]
