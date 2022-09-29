from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Project(models.Model):
    # index = models.AutoField(primary_key=True)
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
