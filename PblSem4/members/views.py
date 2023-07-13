from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.
#
##################### LOGIN TO THE WEBSITE #########################
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Logged in successfully...!"))
            return redirect("profile")
        else:
            messages.success(request,("Enter correct username and password"))
            return redirect("profile")
    else:
        
        return render(request,"authentication/login.html")
    
########################## LOGOUT FROM WEBSITE #############################
def logout_user(request):
    logout(request)
    messages.success(request,("You were loged out...!"))
    return redirect('profile')

####################### REGISTER NEW ADMIN USER ##################################
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Registration Successful...!"))
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request,'authentication/register_user.html',{"form":form})