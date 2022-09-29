from cgitb import text
from turtle import speed
from django.db import models
from project.models import Project

# Create your models here.
class Audio(models.Model):
    # index = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    audio_file = models.FileField(verbose_name="오디오 파일명", null=True)
    speed = models.FloatField(max_length=10)
    update_time = models.DateTimeField(auto_now=True)
    speed = models.IntegerField(default=0)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Text(models.Model):
    text = models.CharField(max_length=300)
    idx = models.IntegerField(verbose_name="텍스트 인덱스")
    audio_id = models.ForeignKey(Audio, on_delete=models.CASCADE)
