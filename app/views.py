from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import *
from .form import *

# Create your views here.
def home(request):
    return render(request, '../templates/register.html')


class subAdmin_register(CreateView):
    model = User
    form_class = subAdminSignUpForm
    template_name = '../templates/customer_register.html'

    def validation(self, form):
        user = form.save()
        login(self.request.user)
        return redirect('/')


class applicant_register(CreateView):
    model = User
    form_class = applicantSignUpForm
    template_name = '../templates/customer_register.html'

    def validation(self, form):
        user = form.save()
        login(self.request.user)
        return redirect('ApplicantDashboard')
