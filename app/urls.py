from django.urls import path
from . import views 

urlpatterns = [
   
    path('', views.home, name='home_page'),
    path('applicant_register', views.applicant_register.as_view(), name='applicant_register'),
    path('subAdmin_register', views.subAdmin_register.as_view(), name='subAdmin_register'),


    
]

