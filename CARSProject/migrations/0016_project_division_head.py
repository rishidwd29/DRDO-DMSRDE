# Generated by Django 4.2.1 on 2023-06-08 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0015_alter_project_extended_pdc_alter_project_pdc'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='division_head',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
