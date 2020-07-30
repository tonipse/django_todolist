from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'complete': forms.CheckboxInput(attrs={'class': 'my-checkbox'}),
            'title': forms.TextInput(attrs={'placeholder': 'Task', 'class': 'center', 'style': 'font-size: 20pt',
                                            'autocomplete': 'new-password'}),

        }
