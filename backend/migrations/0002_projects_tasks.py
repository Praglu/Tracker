# Generated by Django 3.2.5 on 2021-09-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=50)),
                ('projectDescription', models.CharField(max_length=300)),
                ('projectMembers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignedUser', models.CharField(max_length=20)),
                ('projectName', models.CharField(max_length=50)),
                ('taskDescription', models.CharField(max_length=300)),
                ('taskName', models.CharField(max_length=50)),
                ('taskPriority', models.CharField(choices=[('High', 'high'), ('Medium', 'medium'), ('Low', 'low')], default='Low', max_length=7)),
            ],
        ),
    ]