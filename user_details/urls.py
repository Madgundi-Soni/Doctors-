from django.urls import path
from .import views

urlpatterns = [
    path('',views.login_page,name='login_page'),   
    path('patients_signup/',views.patients_signup_view,name='patients_signup_view'),
    path('doc_signup/',views.Doc_signup_view,name='doc_signup_view'),      
    

]
