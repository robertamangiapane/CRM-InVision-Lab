from django.forms import ModelForm
from .models import Collaborator


class AddCollaboratorForm(ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name', 'email', 'phone', 'position', 'availability']
        labels = {'name': "Name", 'email': "Email", 'phone': "Phone", 'position': 'Position', 'availability': "When is available"}
