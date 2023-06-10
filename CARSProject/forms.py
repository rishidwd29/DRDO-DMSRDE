from django.forms import ModelForm
from .models import *

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = '__all__'
