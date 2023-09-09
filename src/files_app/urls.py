from django.urls import path

from .views import (
    FileCreateView,
    FileDeleteView,
    FileDetailView,
    FileListView,
    FileUpdateView,
    run_task,
)

urlpatterns = [
    path("files/new/", FileCreateView.as_view(), name="files_new"),
    path("files/<int:pk>/", FileDetailView.as_view(), name="files_detail"),
    path("files/<int:pk>/edit/", FileUpdateView.as_view(), name="files_edit"),
    path("files/<int:pk>/delete/", FileDeleteView.as_view(), name="files_delete"),
    path("files/runtask/", run_task, name="run_task"),
    path("", FileListView.as_view(), name="home"),
]
