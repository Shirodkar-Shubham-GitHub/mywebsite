from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    
    ctx = {'active_link': 'contact'}
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        # print(name, email, phone, desc)
        ins = Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
        
        return redirect('index')
    return render(request, 'base/index.html', ctx)
