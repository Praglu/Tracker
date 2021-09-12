from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.username}: ({self.password})"


class Projects(models.Model):
    projectName = models.CharField(max_length=50)
    projectDescription = models.CharField(max_length=300)
    projectMembers = models.CharField(max_length=700)

    def __str__(self):
        return f"{self.projectName} | {self.projectDescription} | {self.projectMembers}"


class Tasks(models.Model):
    assignedUser = models.CharField(max_length=20)
    projectName = models.CharField(max_length=50)
    taskDescription = models.CharField(max_length=300)
    taskName = models.CharField(max_length=50)

    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    PRIORITY_CHOICES = [
        (HIGH, "high"),
        (MEDIUM, "medium"),
        (LOW, "low")
    ]
    taskPriority = models.CharField(
        max_length=7, choices=PRIORITY_CHOICES, default=LOW)

    def __str__(self):
        return f"{self.assignedUser} -> {self.projectName} | {self.taskName}, {self.taskDescription} | {self.taskPriority}"
