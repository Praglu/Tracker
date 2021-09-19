from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-users", views.all_users, name="all_users"),
    path("users-only", views.users_only, name="users_only"),
    path("projects", views.projects, name="projects"),
    path("tasks", views.tasks, name="tasks"),
]
