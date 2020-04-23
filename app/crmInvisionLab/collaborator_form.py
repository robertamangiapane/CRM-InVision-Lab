from django.forms import ModelForm, Form
from .models import Collaborator


class AddCollaboratorForm(ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name', 'email', 'phone', 'position', 'availability', 'main_skills']
        labels = {'name': "Name",
                  'email': "Email",
                  'phone': "Phone",
                  'position': 'Position',
                  'availability': "When is available",
                  'main_skills': "Main skills"}

# class SearchCollaboratorForm(Form):
