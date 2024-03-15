from django.contrib.auth.models import AbstractUser
from django.db import models


class Task(models.Model):
    URG = "URGENT"
    HGH = "HIGH"
    MDM = "MEDIUM"
    LOW = "LOW"
    PRIORITY_CHOICES = (
        (URG, "Urgent"),
        (HGH, "High"),
        (MDM, "Medium"),
        (LOW, "LOW")
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="LOW",
    )
    task_type = models.ForeignKey("TaskType", on_delete=models.CASCADE)
    assignees = models.ManyToManyField("Worker", related_name="assignees")

    class Meta:
        ordering = ["priority"]


class TaskType(models.Model):
    name = models.CharField(max_length=255)


class Worker(AbstractUser):
    position = models.ForeignKey("Position", on_delete=models.CASCADE)


class Position(models.Model):
    name = models.CharField(max_length=255)
