from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
# from .models import general_user
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
all_projects  = project.objects.all() # type: ignore
TP = all_projects.count()
form = projectForm()
context = {'CARSlist':all_projects, 'total_projects':TP,'form': form}
def landing(request):
    if request.method == 'POST':
        projectid = request.POST['project id']
        projecttitle = request.POST['project title']
        divisionhead = request.POST['division head']
        buildupprojectid= request.POST['build up projectid']
        CARScoordinator = request.POST['CARS coordinator']
        totalcost = request.POST['total cost']
        irsp = request.POST['irsp']
        carsl1selected = request.POST['carsl1selected']
        
        addproject = project(project_id = projectid, Title_of_Project = projecttitle, 
        division_head = divisionhead, project_no_buildup = buildupprojectid)
        addproject.save()
        redirect('/')
        
    return render(request, 'CARSProject/landing.html', context)

def admin(request):
    return redirect("/admin")
def dashboard(request):
    return render(request, 'CARSProject/Dashboard.html', context )
def GSQR(request):
    gsqrlist = gsqr.objects.all()
    return render(request, 'CARSProject/GSQR.html', {'GSQRlist':gsqrlist})
def generate(request):
    return render(  request,'CARSProject/generate.html', context)

def projects(request, pk):
    projects = project.objects.get(project_id=pk)
    return render(request, 'CARSProject/project.html', {'projects': projects,'total_projects': TP })

def CreateProject(request):
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
                    form.save()
                    messages.success(request, 'Project Created Successfully')
                    return redirect('/')
    return render(request, 'CARSProject/project_form.html', context)

def updateproject(request, pk):
    update = project.objects.get(project_id=pk)
    form = projectForm(instance=update)
    if request.method == 'POST':
        form = projectForm(request.POST, instance=update)
        if form.is_valid():
                    form.save()
                    messages.success(request, 'Project Created Successfully')
                    return redirect('/')
    return render(request, 'CARSProject/project_form.html', {"update":update, 'total_projects': TP, "form":form})