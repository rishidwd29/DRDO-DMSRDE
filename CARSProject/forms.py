from django.forms import ModelForm
from .models import *

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = '__all__'

class pdfsubmit(ModelForm):
    class Meta:
        model = project
        fields = ['irsp']
        
        
        
class rsqrcommityform(ModelForm):
    class Meta :
        model = project
        fields = ['rsqrdoc', 'objective', 'justification', 'plan_of_work',
                  'milestones', 'project_investigator','duration',
                  'chairman', 'member_1', 'member_2', 'member_3',
                  'member_secretory','minsheet'
                  ]
        
        
        
        
        
        
        
class rsqrpdf(ModelForm):
    class Meta:
        model = project
        fields = ['rsqrdoc']
class minpdf(ModelForm):
    class Meta:
        model = project
        fields = ['minsheet']