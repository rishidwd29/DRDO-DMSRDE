# Generated by Django 4.2.1 on 2023-06-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0031_rename_total_cost_project_estimate_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='annexure_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='annexure_2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
