from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from contactapp.models import contactmodel, videomodel

def index(request):
    video=videomodel.objects.all()
    return render(request,"index.html",{'vi':video})

def main(request):
    video=videomodel.objects.all()
    return render(request,"main.html",{'vi':video})    

@login_required(login_url='adminlogin')   
def adminpage(request):
    tcon=contactmodel.objects.all().count()
    ncon=contactmodel.objects.all().filter(status=False).count()
    dict={'tcon':tcon,'ncon':ncon}
    return render(request,"adminpage.html",context=dict)

@login_required(login_url='adminlogin')   
def signout(request):
	auth.logout(request)
	return redirect('admin')   

def insertcontact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        num=request.POST['num']
        msg=request.POST['msg']
        data=contactmodel(name=name,email=email,mobile=num,message=msg)
        data.save()
        messages.success(request, "Your Details Submitted Successfully") 
        return redirect('index')    
    return redirect('index')     

@login_required(login_url='adminlogin')   
def admincontact(request):
    con=contactmodel.objects.all()
    for i in con:
        i.status=True
        i.save()   
    return render(request,"admincontact.html",{'con':con})

@login_required(login_url='adminlogin')   
def deletecontact(request,pk):
    app=contactmodel.objects.get(id=pk)
    app.delete()
    return redirect('admincontact') 

@login_required(login_url='adminlogin')   
def adminvideo(request):
    return render(request,"adminvideo.html")    

def admin(request):
    return render(request,"admin.html")     

@login_required(login_url='adminlogin')   
def insertvideo(request):
    if request.method=='POST':
        video=request.FILES['file']
        videomodel.objects.all().delete()
        data=videomodel(video=video)
        data.save()
        messages.info(request, 'Your video uploaded succesfully')
    return redirect('adminvideo') 

def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
                auth.login(request,user)
                return redirect('adminpage')
        else:
                messages.info(request, 'Invalid Username or Password. Try Again.')
                return redirect('admin')
    return redirect('admin')             
                    