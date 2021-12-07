from django.shortcuts import render

# Create your views here.
def ApplicantDashboard(request):
    return render(request, 'applicantdashoard.html')