from django.urls import path

from .views import FileCreateView, FileDetailView, FileListView, FileUpdateView

urlpatterns = [
    path("files/new/", FileCreateView.as_view(), name="files_new"),
    path("files/<int:pk>/", FileDetailView.as_view(), name="files_detail"),
    path("files/<int:pk>/edit/", FileUpdateView.as_view(), name="files_edit"),
    path("", FileListView.as_view(), name="home"),
]
