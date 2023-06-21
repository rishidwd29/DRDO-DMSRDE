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
class rsqrpdf(ModelForm):
    class Meta:
        model = project
        fields = ['rsqrdoc']
class minpdf(ModelForm):
    class Meta:
        model = project
        fields = ['minsheet']