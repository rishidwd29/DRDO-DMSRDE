# Generated by Django 4.2.1 on 2023-06-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0016_project_division_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_of_start',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
