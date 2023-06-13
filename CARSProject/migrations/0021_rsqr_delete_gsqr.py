# Generated by Django 4.2.1 on 2023-06-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0020_alter_project_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='rsqr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=225)),
                ('justification', models.CharField(max_length=500)),
                ('plan_of_work', models.CharField(max_length=600)),
                ('milestones', models.CharField(max_length=600)),
                ('project_investigator', models.CharField(max_length=500)),
                ('duration', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='gsqr',
        ),
    ]