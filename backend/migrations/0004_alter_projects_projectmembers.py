# Generated by Django 3.2.5 on 2021-09-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_projects_projectmembers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='projectMembers',
            field=models.TextField(),
        ),
    ]