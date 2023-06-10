# Generated by Django 4.2.1 on 2023-05-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Buildup', models.CharField(max_length=500)),
                ('Project_ID', models.PositiveIntegerField(default=0)),
                ('Start_date', models.DateField(auto_now=True)),
                ('Interested_institutes', models.CharField(max_length=800)),
                ('RSQR', models.CharField(max_length=50)),
                ('Total_cost', models.PositiveIntegerField()),
            ],
        ),
    ]