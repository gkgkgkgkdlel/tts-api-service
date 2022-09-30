from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.CreateAudioView.as_view()),
    path("read/", views.ReadTextView.as_view()),
    path("update/", views.UpdateTextView.as_view()),
    path("audio_file/", views.GetAudioFileView.as_view()),
    path("insert_audio_file/", views.InsertTextView.as_view()),
    path(
        "delete/<int:project_id>/",
        views.DeleteProjectView.as_view(),
    ),
]
