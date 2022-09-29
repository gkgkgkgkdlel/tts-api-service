# Generated by Django 4.1.1 on 2022-09-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("project_id", models.AutoField(primary_key=True, serialize=False)),
                ("project_title", models.CharField(max_length=100)),
                ("update_time", models.DateTimeField(auto_now=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
