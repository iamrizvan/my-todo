from django import forms
from django.forms import ModelForm
from django.forms import fields

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
