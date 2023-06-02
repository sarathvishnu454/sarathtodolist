from django import forms

from .models import todolist



class updateform(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['name', 'date', 'priority']