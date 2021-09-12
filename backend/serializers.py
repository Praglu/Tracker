from rest_framework import serializers
from .models import Users, Projects, Tasks


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'projectName', 'projectDescription', 'projectMembers')


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'assignedUser', 'projectName',
                  'taskDescription', 'taskName', 'taskPriority')
