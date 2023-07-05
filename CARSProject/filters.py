import django_filters 
from . models import *

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = project
        fields = ['project_id','Title_of_Project','division_head','project_no_buildup','carscoordinator',
                  'irsp','carsl1selectedinstitutes','date_of_start','chairman',
                  'Objective','justication','project_investigator',
                  'member_1','member_2','member_3','member_secratory',
                  'installatment_1_date','installment_1_amount','cheque_no_1',
                  'Equipment_Issued_at_Installment_1','Installment_1_expenditure_statement'
                  'installatment_2_date','installment_2_amount','cheque_no_2',
                  'Equipment_Issued_at_Installment_2','Installment_2_expenditure_statement'
                  'installatment_3_date','installment_3_amount','cheque_no_3',
                  'Equipment_Issued_at_Installment_3','Installment_3_expenditure_statement'
                  'installatment_4_date','installment_4_amount','cheque_no_4',
                  'Equipment_Issued_at_Installment_4','Installment_4_expenditure_statement'
                  ]