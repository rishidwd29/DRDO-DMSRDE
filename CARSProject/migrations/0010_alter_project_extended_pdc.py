# Generated by Django 4.2.1 on 2023-06-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0009_alter_project_scantion_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='extended_pdc',
            field=models.FloatField(blank=True, null=True),
        ),
    ]