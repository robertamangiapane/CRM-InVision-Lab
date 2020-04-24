from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Collaborator


class AddCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name', 'email', 'phone', 'position', 'availability', 'main_skills', 'secondary_skills']
        labels = {'name': "Name",
                  'email': "Email",
                  'phone': "Phone",
                  'position': 'Position',
                  'availability': "When is available",
                  'main_skills': "Main skills",
                  'secondary_skills': "Secondary skills"}


class SearchCollaboratorForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(max_length=200, required=False)
    phone = PhoneNumberField(max_length=200, required=False)
    position = forms.CharField(max_length=200, required=False)
    availability = forms.CharField(max_length=200, required=False)
    main_skills = forms.CharField(max_length=200, required=False)
    secondary_skills = forms.CharField(max_length=200, required=False)

