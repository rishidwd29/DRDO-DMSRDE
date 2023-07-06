import django_filters 
from . models import *
from django.forms import DateInput
from django_filters import DateFilter

class ProjectFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date_of_start", lookup_expr='gte')
    end_date = DateFilter(field_name = "date_of_start", lookup_expr='lte')
    class Meta:
        model = project
        fields = ['project_id','Title_of_Project','division_head','project_no_buildup','carscoordinator',
                  'carsl1selectedinstitutes','chairman',
                  'objective','justification','project_investigator',
                  'member_1','member_2','member_3','member_secretory',
                  'installment_1_date','cheque_no_1',
                  'Equipment_Issued_at_Installment_1','Installment_1_expenditure_statement',
                  'installment_2_date','cheque_no_2',
                  'Equipment_Issued_at_Installment_2','Installment_2_expenditure_statement',
                  'installment_3_date','cheque_no_3',
                  'Equipment_Issued_at_Installment_3','Installment_3_expenditure_statement',
                  'installment_4_date','cheque_no_4',
                  'Equipment_Issued_at_Installment_4','Installment_4_expenditure_statement',
                  ]
        widgets = {
            'date_of_start': DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )}