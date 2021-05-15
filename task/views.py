from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from task.forms import TaskForm
from task.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Task.objects.filter(user=self.request.user)

        # filtered user related tasks
        context['tasks'] = user_tasks

        # count user's incomplete tasks
        context['incomplete_count'] = user_tasks.filter(completed=False).count()

        # search tasks
        search_value = self.request.GET.get('search') or ''
        if search_value:
            context['tasks'] = user_tasks.filter(title__icontains=search_value)

        context['search_value'] = search_value
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/task.html'

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user.id != request.user.id:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_text'] = 'Add Task'
        context['button_text'] = 'Add'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:index')

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user.id != request.user.id:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_text'] = 'Update Task'
        context['button_text'] = 'Update'
        return context

    def form_valid(self, form):
        if form.instance.user.id != self.request.user.id:
            raise PermissionDenied
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task:index')

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user.id != request.user.id:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user.id != request.user.id:
            raise PermissionDenied
        return super().delete(request, *args, **kwargs)
