from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from task.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'due_date',
            'completed',
        )
        widgets = {'due_date': DateInput()}

    def clean_due_date(self):
        """Validate task due date."""
        due_date = self.cleaned_data['due_date']
        if due_date < timezone.now().date():
            raise ValidationError("Due date should not before today!")
        return due_date
