from django.urls import path
from . import views 

urlpatterns = [
   
   
    path('applicant_dashboard', views.ApplicantDashboard, name='applicant_dashboard'),


    
]