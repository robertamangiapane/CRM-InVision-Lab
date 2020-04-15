from django import forms
from django.forms import ModelForm
from .models import Collaborator


class AddCollaboratorForm(ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name', 'email', 'phone', 'position', 'availability', 'main_skills', 'secondary_skills']

