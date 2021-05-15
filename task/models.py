import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):
    """A model to represent a task."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False, verbose_name='Mark as completed')
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['completed', '-created_datetime']

    def __str__(self):
        """Return string representation of task."""
        return self.title

    @property
    def is_overdue(self):
        """Check task overdue."""
        return timezone.now().date() > self.due_date
