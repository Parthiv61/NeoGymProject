from django.shortcuts import render
from .forms import contact_model
from django.core.mail import send_mail
from  neogym import settings


def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
        newuser=contact_model(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("Thanks")
            
            #Email Sending Code
            sub="Welcome"
            msg=f"Dear User!\nThank you for your patience\nWe will contact you in shortly\nFor any query,contact on\n+91 9924761666"
            from_email=settings.EMAIL_HOST_USER
            to_mail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_mail)
            
            
        else:
            print(newuser.errors)
    return render(request,'contact.html')

def trainer(request):
    return render(request,'trainer.html')

def why(request):
    return render(request,'why.html')
