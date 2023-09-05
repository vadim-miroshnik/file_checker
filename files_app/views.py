from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Files


class FileListView(ListView):
    model = Files
    template_name = "home.html"


class FileDetailView(DetailView):
    model = Files
    template_name = "files_detail.html"


class FileCreateView(CreateView):
    model = Files
    template_name = "files_new.html"
    fields = ["name", "author", "file"]


class FileUpdateView(UpdateView):
    model = Files
    template_name = "files_edit.html"
    fields = ["name", "file"]
