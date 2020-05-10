from django.shortcuts import render
from .models import Userpi,User
from .forms import Userpif,Userform
# Create your views here.

def index(request):
    info = User.objects.all()
    return render(request,'index.html',{'info':info})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = Userform(data=request.POST)
        profile_form = Userpif(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            #profile.save()
            registered = True
            return render(request,'registration.html')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = Userform()
        profile_form = Userpif()
    return render(request,'registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
