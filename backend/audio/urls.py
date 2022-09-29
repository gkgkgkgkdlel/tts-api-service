from django.urls import path
from . import views


urlpatterns = [
    path("test/", views.TextView.as_view()),
    path("create/", views.CreateAudioView.as_view()),
]
