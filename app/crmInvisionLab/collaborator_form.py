from django import forms
from .models import Collaborator


class AddCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name', 'email', 'phone', 'position', 'availability', 'main_skills']
        labels = {'name': "Name",
                  'email': "Email",
                  'phone': "Phone",
                  'position': 'Position',
                  'availability': "When is available",
                  'main_skills': "Main skills"}


class SearchCollaboratorForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    email = forms.CharField(max_length=200, required=False)
    phone = forms.CharField(max_length=200, required=False)
    position = forms.CharField(max_length=200, required=False)
    availability = forms.CharField(max_length=200, required=False)
    main_skills = forms.CharField(max_length=200, required=False)

