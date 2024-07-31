from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/<int:id>/',views.Doctor_dashboard,name='doctor_dashboard'),   
    path('logout_view/',views.logout_view,name='logout_view'),   
    
]
