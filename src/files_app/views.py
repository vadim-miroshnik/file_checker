from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Coalesce
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import File


class FileListView(LoginRequiredMixin, ListView):
    model = File
    template_name = "home.html"

    def get_queryset(self):
        return File.objects.filter(author=self.request.user).order_by(
            Coalesce("modified", "created").asc()
        )


class FileDetailView(LoginRequiredMixin, DetailView):
    model = File
    template_name = "files_detail.html"


class FileCreateView(LoginRequiredMixin, CreateView):
    model = File
    fields = ["file"]
    template_name = "files_new.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.name = form.instance.file.name
        return super(FileCreateView, self).form_valid(form)


class FileUpdateView(LoginRequiredMixin, UpdateView):
    model = File
    template_name = "files_edit.html"
    fields = ["name", "file"]

    def form_valid(self, form):
        form.instance.status = File.FileStatus.CREATED
        return super().form_valid(form)


class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = File
    template_name = "files_delete.html"
    success_url = reverse_lazy("home")
