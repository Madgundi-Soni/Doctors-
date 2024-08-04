from django.urls import path
from .import views
from django.contrib.auth import authenticate, login,logout

urlpatterns = [
    path('dashboard/<int:id>/',views.Patient_dashboard,name='patient_dashboard'),   
    path('logout_view/',views.logout_view,name='logout_view'),   
    path('blogs_list/',views.Blogs_list,name='blogs_list'),   

]
