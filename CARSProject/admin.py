from django.contrib import admin
from .models import *
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(project)

class projectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(models.project, projectAdmin)


