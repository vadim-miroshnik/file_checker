from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Files


class FileListView(ListView):
    model = Files
    template_name = "home.html"


class FileDetailView(DetailView):
    model = Files
    template_name = "files_detail.html"


class FileCreateView(CreateView):
    model = Files
    fields = ["file"]
    template_name = "files_new.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.name = form.instance.file.name
        return super(FileCreateView, self).form_valid(form)


class FileUpdateView(UpdateView):
    model = Files
    template_name = "files_edit.html"
    fields = ["name", "file"]


class FileDeleteView(DeleteView):
    model = Files
    template_name = "files_delete.html"
    success_url = reverse_lazy("home")
