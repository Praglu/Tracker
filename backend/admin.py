from django.contrib import admin
from .models import Users, Projects, Tasks

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list = ('username', 'password')


class ProjectsAdmin(admin.ModelAdmin):
    list = ('projectName', 'projectDescription', 'projectMembers')


class TasksAdmin(admin.ModelAdmin):
    list = ('assignedUser', 'projectName', 'taskDescription', 'taskName', 'taskPriority')


admin.site.register(Users, UsersAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Tasks, TasksAdmin)