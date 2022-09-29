from cgitb import text
from turtle import speed
from django.db import models


# Create your models here.


class Project(models.Model):
    # index = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)


class Audio(models.Model):
    # index = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    audio_file = models.FileField(verbose_name="오디오 파일명", null=True)
    speed = models.FloatField(max_length=10, default=1.0)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now=True)


class Text(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    idx = models.IntegerField(verbose_name="텍스트 인덱스")
    audio_id = models.ForeignKey(Audio, on_delete=models.CASCADE)


class TextList(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_idx = models.IntegerField(verbose_name="문장 인덱스", default=0)
    text_id = models.ForeignKey(Text, on_delete=models.CASCADE)
    sentence = models.TextField()
