# Generated by Django 4.2.1 on 2023-06-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARSProject', '0019_alter_project_project_no_buildup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
