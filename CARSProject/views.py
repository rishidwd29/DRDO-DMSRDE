from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
# from .models import general_user
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,FileResponse
from django.contrib import messages
from .models import *
from .forms import *
from .filters import *
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

all_projects  = project.objects.all() # type: ignore
TP = all_projects.count()
form = projectForm()

context = {'CARSlist':all_projects, 'total_projects':TP,'form': form, 'formsub': pdfsubmit()}

def process(request):
    cid = 0 
    if request.method == "POST":
        currentid = request.POST['projectid']
        cid = str(currentid)
        print (cid)
    return render(request, 'CARSProject/process.html',{'total_projects': TP,'currentid':cid})

def closer(request,pk):
    update = project.objects.get(project_id=pk)
    closerForm = closerform(instance=update)
    if request.method == 'POST':
        closerForm = closerform(request.POST, request.FILES,instance=update)
        if closerForm.is_valid():
                    closerForm.save()
                    redirect('/process')
                    messages.success(request, 'details added Successfully')    
    return render(request ,'CARSProject/closer.html', {'total_projects':TP,'closerForm':closerForm})

def installment(request, pk):
    update = project.objects.get(project_id=pk)
    installmentForm = installmentform(instance=update)
    if request.method == 'POST':
        installmentForm = installmentform(request.POST, request.FILES,instance=update)
        if installmentForm.is_valid():
                    installmentForm.save()
                    redirect('/process')
                    messages.success(request, 'details added Successfully')    
    return render(request, 'CARSProject/installment.html',{'total_projects':TP,'installmentform':installmentForm})
def annexure(request, pk):
    update = project.objects.get(project_id=pk)
    annexureform = annexureForm(instance=update)
    if request.method == 'POST':
        annexureform = annexureForm(request.POST, request.FILES,instance=update)
        if annexureform.is_valid():
                    annexureform.save()
                    redirect('/process')
                    messages.success(request, 'details added Successfully')    
    return render(request, 'CARSProject/annexure.html',{'total_projects': TP,'annexureform':annexureform})
def rsqrcommity(request,pk):
    update = project.objects.get(project_id=pk)
    rsqrform = rsqrcommityform(instance=update)
    if request.method == 'POST':
        rsqrform = rsqrcommityform(request.POST, request.FILES,instance=update)
        if rsqrform.is_valid():
                    rsqrform.save()
                    messages.success(request, 'details added Successfully')
        
    # if request.method == "POST":
    #     rsqrform = rsqrpdf(request.POST, request.FILES)
    #     if rsqrform.is_valid():
    #         rsqrform.save()
    # if request.method == "POST":
    #     min_pdf = minpdf(request.POST, request.FILES)
    #     if min_pdf.is_valid():
    #         min_pdf.save()
    
    # if request.method == 'POST':
    #     objective = request.POST['objective']
    #     justification = request.POST['justification']
    #     methodology = request.POST['methodology']
    #     Milestone = request.POST['milestone']
    
    #     project_investigator = request.POST['project investigator']
    #     # total_cost = request.POST['total cost']
    #     duration = request.POST['duration']
    #     deliverables = request.POST['deliverables']

    #     Chairman = request.POST['chairman']
    #     member1 = request.POST['member1']
    #     member2 = request.POST['member2']
    #     member3 = request.POST['member3']
    #     Membersec = request.POST['members secratory']

        
    #     addrsqr= project(objective = objective, justification= justification,
    #                   plan_of_work = methodology,milestones= Milestone,
    #                   project_investigator = project_investigator,
    #                   duration = duration,chairman=Chairman, member_1 = member1,
    #                   member_2 = member2, member_3= member3, member_secretory= Membersec)
    #     addrsqr.save()
    
    return render (request, 'CARSProject/rsqrcommity.html', {'total_projects':TP,'rsqrform': rsqrform})

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
    

def landing(request):
    cid = 0
    if request.method == 'POST':
        projectid = request.POST['project id']
        cid =projectid
        projecttitle = request.POST['project title']
        divisionhead = request.POST['division head']
        buildupprojectid= request.POST['build up projectid']
        CARScoordinator = request.POST['CARS coordinator']
        Estimate_Cost = request.POST['total cost']
        
        carsl1selected = request.POST['carsl1selected']
        addproject = project(project_id = projectid, Title_of_Project = projecttitle, 
            division_head = divisionhead, project_no_buildup = buildupprojectid, 
            Estimate_Cost = Estimate_Cost,carscoordinator = CARScoordinator,carsl1selectedinstitutes = carsl1selected )
        addproject.save()
    if request.method == "POST":
        update = project.objects.get(project_id = cid)
        pdform = pdfsubmit(instance=update,)
        if request.method == "POST":
            pdform = pdfsubmit(request.POST, request.FILES,instance= update)
            if pdform.is_valid():
                pdform.save()
            
        
    return render(request, 'CARSProject/landing.html', context)

def admin(request):
    return redirect("/admin")
def dashboard(request):
    allprojects = project.objects.all()
    myFilter = ProjectFilter(request.GET, queryset=allprojects)
    allprojects = myFilter.qs
    return render(request, 'CARSProject/Dashboard.html', 
        {'total_projects':TP,'allprojects':allprojects,'myFilter':myFilter} )
   
def generate(request):
    return render(  request,'CARSProject/generate.html', context)

def projects(request, pk):
     
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