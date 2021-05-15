from django.urls import path

from task.views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    # path('task/<uuid:pk>/', TaskDetailView.as_view(), name='task'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<uuid:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<uuid:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
