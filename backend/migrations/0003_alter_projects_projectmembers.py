# Generated by Django 3.2.5 on 2021-09-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_projects_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='projectMembers',
            field=models.CharField(max_length=700),
        ),
    ]
