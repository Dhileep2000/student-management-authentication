from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views.decorators.csrf import requires_csrf_token


def loginpage(request):

    context={
        "error":""
    }

    if request.method == "POST":
        print(request.POST)

        user = authenticate(username=request.POST["username"],password=request.POST["password"])
        print(user)

        if user != None:
            login(request,user)
            return redirect('/student/manage/')
        
        else:
            
            context={
                "error":"*invalid username and password"
            }
            return render(request,"login.html",context)


    return render(request,'login.html',context)



def logoutpage(request):
    
    logout(request)
    return redirect("/")



def signup(request):


    if request.method == "POST":

        new_user=student_model.objects.filter(username=request.POST['user_name'])

        if len(new_user)>0:
            context={
                "error":"already exit name"
            }
            return render(request,'signup.html',context)
        
        else:

            user=student_model(username=request.POST['user_name'],email=request.POST['email'])

            user.set_password(request.POST['password'])
            user.save()
            return redirect("/")   

    return render(request,'signup.html')



