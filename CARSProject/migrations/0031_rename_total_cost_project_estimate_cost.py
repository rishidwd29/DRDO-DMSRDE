# Generated by Django 4.2.1 on 2023-06-27 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0030_alter_project_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='total_cost',
            new_name='Estimate_Cost',
        ),
    ]
