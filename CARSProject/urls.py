"""ProjectManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'initialize'),
    # path('irspcommity', views.irspcommity, name ='irspcommity'),444
    path('project/<str:pk>/', views.projects, name = 'project'), 
    path('projectpdf/', views.projectpdf, name = 'projectpdf'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('process/', views.process, name = 'process'),
    path('rsqrcommity/<str:pk>', views.rsqrcommity, name = 'rsqrcommity'),
    path('annexure/<str:pk>', views.annexure, name = 'annexure'),
    
    path('generate/', views.generate, name = 'generate'),
    path('create_project/', views.CreateProject, name = "create_project"),
    path('update_project/<str:pk>/', views.updateproject, name = "updateproject")
]
