import datetime
from django.db import models

# Create your models here.
class project(models.Model):
    project_id  = models.IntegerField( primary_key=True,)
    Title_of_Project = models.CharField(max_length = 500, null = True, blank = True)
    division_head = models.CharField(max_length = 600, null = True, blank = True)
    project_no_buildup = models.CharField(max_length= 400,null = True ,blank=True)
    carscoordinator = models.CharField(max_length = 100, null = True, blank=True)
    total_cost = models.FloatField(default=0,null = True, blank=True)
    irsp = models.FileField(null=True, blank = True)
    carsl1selectedinstitutes = models.CharField(max_length = 500, null= True, blank=True)
    initial_sanction_cost = models.FloatField(default=0,null = True, blank=True)
    date_of_start = models.DateField(auto_now_add = True,null = True, blank=True)
    pdc = models.DateField(null = True, blank=True)
    nomination_rsp = models.CharField(max_length=100,null = True, blank=True)
    date_of_complition = models.DateField(null = True, blank=True)
    extended_pdc =  models.DateField(blank= True, null = True)
    no_of_publications = models.FloatField(default= 0,null = True, blank=True)
    no_of_irsp_Filed = models.FloatField(blank= True, default=0,null = True)
    trained_manpower = models.PositiveBigIntegerField(blank=True , default=0,null = True)
    domain_lab = models.CharField(max_length=500,null = True, blank=True)
    cluster = models.CharField(max_length=100, blank=True,null = True)
    scantion_year = models.PositiveIntegerField(null = True, blank=True)
    current_status = models.CharField(max_length=1000 , blank = True,null = True)
    date_of_closure = models.DateField(null = True, blank=True)
    # Interested_institutes = models.CharField(max_length= 800, blank=True)
    cost_in_lakh =models.FloatField(null = True, blank=True)
    advance_date = models.DateField(null = True, auto_now=True, blank=True)
    advnace_amount = models.FloatField(null = True, blank=True)
    dv_no_cheque_slip_no = models.FloatField(null  = True, blank=True)
    cheque_date = models.DateField(null = True, blank=True)
    installment_1_date = models.DateField(null = True, blank=True)
    installment_1_amount = models.FloatField(null = True, blank=True)
    cheque_no_date = models.CharField(null = True, max_length= 500, blank=True)
    installment_2_date = models.DateField(null = True, blank=True)
    installment_2_amount = models.FloatField(null = True, blank=True)
    cheque_no_date = models.CharField(null = True, max_length=500, blank=True)
    installment_3_date = models.DateField(null = True, blank=True)
    installment_3_amount = models.FloatField(null = True, blank=True)
    cheque_no_date = models.CharField(null = True, max_length=500, blank=True)
    installment_4_date = models.DateField(null = True, blank=True)
    installment_4_amount = models.FloatField(null = True, blank=True)
    cheque_no_date = models.CharField(null = True, max_length=500, blank=True)
    total_amount_released = models.FloatField(null = True, blank=True)
    unutilized_amount = models.FloatField(null=True, blank=True)
    total_utilized_amount = models.FloatField(null = True, blank=True)
    

#      Pojects = models.ForeignKey(projects, on_delete= models.CASCADE)
#     Project_ID = models.FloatField(models.ForeignKey(projects, on_delete=models.CASCADE))
#     Installments = models.PositiveSmallIntegerField(default=0)
#     Installment_sum = models.PositiveBigIntegerField(blank = False)
def __str__(self):
    return self.Project_ID


class rsqr(models.Model):
    objective = models.CharField(max_length = 225)
    justification = models.CharField(max_length =500)
    plan_of_work = models.CharField(max_length = 600)
    milestones = models.CharField(max_length= 600)
    project_investigator = models.CharField(max_length = 500)
    duration = models.CharField(max_length = 500)
def __obj__(self):
    return self.objective