from django.forms import ModelForm
from .models import *
from django.forms import DateInput

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
        
        
class annexureForm(ModelForm):
    class Meta:
        model = project
        fields = ['annexure_1', 'annexure_2']
        
        
        
class installmentform(ModelForm):
    class Meta :
        model = project
        fields = ['installment_1_date', 'installment_1_amount','cheque_no_1','Equipment_Issued_at_Installment_1','Installment_1_expenditure_statement',
                  'installment_2_date', 'installment_2_amount','cheque_no_2','Equipment_Issued_at_Installment_2','Installment_2_expenditure_statement',
                  'installment_3_date', 'installment_3_amount','cheque_no_3','Equipment_Issued_at_Installment_3','Installment_3_expenditure_statement',
                  'installment_4_date', 'installment_4_amount','cheque_no_4','Equipment_Issued_at_Installment_4','Installment_4_expenditure_statement',
                  'total_amount_released',
                  ]
        widgets = {
            'installment_1_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'installment_2_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'installment_3_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'installment_4_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
class closerform(ModelForm):
    class Meta :
        model = project
        fields = [
            'date_of_complition',
            'total_utilized_amount',
            'closure_report'
                ]
        widgets = {
            'date_of_complition': DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )}
        
        
class rsqrpdf(ModelForm):
    class Meta:
        model = project
        fields = ['rsqrdoc']
class minpdf(ModelForm):
    class Meta:
        model = project
        fields = ['minsheet']
        