# Generated by Django 4.2.1 on 2023-07-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0035_remove_project_cost_in_lakh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
