from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
# from .models import general_user
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,FileResponse
from django.contrib import messages
from .models import *
from .forms import *
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def projectpdf(request):
    # create a byte stream buffer
    buf = io.BytesIO()
    # create canvas
    c = canvas.Canvas(buf,pagesize = letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica", 14)
    lines = [
        "this is line one"
    ]
    for line in lines:
        textob.textLine(line)
    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename="test.pdf")

all_projects  = project.objects.all() # type: ignore
TP = all_projects.count()
form = projectForm()
formsub = pdfsubmit()
context = {'CARSlist':all_projects, 'total_projects':TP,'form': form, 'formsub': formsub}
def landing(request):
    if request.method == 'POST':
        projectid = request.POST['project id']
        projecttitle = request.POST['project title']
        divisionhead = request.POST['division head']
        buildupprojectid= request.POST['build up projectid']
        CARScoordinator = request.POST['CARS coordinator']
        totalcost = request.POST['total cost']
        
        carsl1selected = request.POST['carsl1selected']
        addproject = project(project_id = projectid, Title_of_Project = projecttitle, 
            division_head = divisionhead, project_no_buildup = buildupprojectid, 
            total_cost = totalcost,carscoordinator = CARScoordinator,carsl1selectedinstitutes = carsl1selected )
        addproject.save()
    if request.method == "POST":
        pdform = pdfsubmit(request.POST, request.FILES)
        if pdform.is_valid():
            pdform.save()
        
    return render(request, 'CARSProject/landing.html', context)

def admin(request):
    return redirect("/admin")
def dashboard(request):
    return render(request, 'CARSProject/Dashboard.html', context )
def irspcommity(request):
    if request.method == 'POST':
        objective = request.POST['objective']
        justification = request.POST['justification']
        methodology = request.POST['methodology']
        Milestone = request.POST['milestone']
        project_investigator = request.POST['project investigator']
        # total_cost = request.POST['total cost']
        duration = request.POST['duration']
        deliverables = request.POST['deliverables']

        Chairman = request.POST['chairman']
        member1 = request.POST['member1']
        member2 = request.POST['member2']
        member3 = request.POST['member3']
        Membersec = request.POST['members secratory']

        
        addrsqr= irsp(objective = objective, justification= justification,
                      plan_of_work = methodology,milestones= Milestone,
                      project_investigator = project_investigator,
                      duration = duration,chairman=Chairman, member_1 = member1,
                      member_2 = member2, member_3= member3, member_secretory= Membersec)
        addrsqr.save()
        return redirect('/generate')
        
    return render (request, 'CARSProject/irspcommity.html', context)
    
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