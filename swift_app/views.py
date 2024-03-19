from django.shortcuts import render, redirect
from .models import package
# Create your views here.

def home(request):
    if request.method == "POST":
        try:
            tracking_id= request.POST['tracking_id']
        except:
            redirect("home")
      
    return render(request, "index.html", {})
    
def packagedetails(request, tracking_id):
    packageinfo= package.objects.get(Tracking_Id= tracking_id)
    
    return render(request, "package_details.html", {"packageinfo": packageinfo})
    