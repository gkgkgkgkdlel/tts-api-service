from django.urls import path
from . import views


urlpatterns = [
    path("test/", views.TextView.as_view()),
    path("create/", views.CreateAudioView.as_view()),
    path("read/", views.ReadTextView.as_view()),
    path("update/", views.UpdateTextView.as_view()),
]
