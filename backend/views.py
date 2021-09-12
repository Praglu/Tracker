from django.shortcuts import render
import psycopg2
from .serializers import UsersSerializer, ProjectsSerializer, TasksSerializer
from rest_framework import serializers, viewsets
from .models import Users, Projects, Tasks


# Create your views here.


def homepage(request):
    # connection = psycopg2.connect(
    #     "dbname=tracker user=postgres password=PostgreSQLDupa@38844")

    # cursor = connection.cursor()

    # cursor.execute("""
    # SELECT
	# u.user_id, u.username,
	# p.project_id, p.project_name, p.project_description,
	# t.task_id, t.task_name
    # FROM users u
    # JOIN users_projects AS up ON u.user_id = up.user_id
    # JOIN projects AS p ON up.project_id = p.project_id
    # JOIN projects_tasks AS pt ON p.project_id = pt.project_id
    # JOIN tasks AS t ON pt.task_id = t.task_id
    #         """)

    # records = cursor.fetchall()

    return render(request, 'index.html', {
        # "records": records
    })


class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class ProjectsView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()


class TasksView(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
