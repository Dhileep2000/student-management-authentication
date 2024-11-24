from django.shortcuts import render,redirect
from .models import *
from .forms import *




def studentmanage(request):

    student_data=studentmodel.objects.all()

    return render(request,'student_management.html',{'student_data': student_data})

def update(request,id):

    if request.method == "POST":
        student=studentmodel.objects.get(pk=id)
        fm=studentform(request.POST,instance=student)

        if fm.is_valid():
            fm.save()
            return redirect('/student/manage/')
    
    else:
        student=studentmodel.objects.get(pk=id)
        fm=studentform(instance=student)

    return render(request,'student_update.html',{"forms":fm})

def delete(request,id):

    if request.method == "POST":
        student=studentmodel.objects.get(pk=id)
        student.delete()

    return redirect("/student/manage/")

def addpage(request):


    fm=studentform()

    if request.method == "POST":
        fm=studentform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/student/manage/")

    return render(request,'add.html',{"form":fm})

