from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Files


class FileListView(LoginRequiredMixin, ListView):
    model = Files
    template_name = "home.html"

    def get_queryset(self):
        return Files.objects.filter(author=self.request.user).order_by(
            Coalesce("modified", "created").asc()
        )


class FileDetailView(LoginRequiredMixin, DetailView):
    model = Files
    template_name = "files_detail.html"


class FileCreateView(LoginRequiredMixin, CreateView):
    model = Files
    fields = ["file"]
    template_name = "files_new.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.name = form.instance.file.name
        return super(FileCreateView, self).form_valid(form)


class FileUpdateView(LoginRequiredMixin, UpdateView):
    model = Files
    template_name = "files_edit.html"
    fields = ["name", "file"]

    def form_valid(self, form):
        form.instance.status = Files.FileStatus.CREATED
        return super().form_valid(form)


class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = Files
    template_name = "files_delete.html"
    success_url = reverse_lazy("home")
