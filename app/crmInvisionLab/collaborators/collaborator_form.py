from django import forms
from phonenumber_field.formfields import PhoneNumberField
from ..models import Collaborator, Skill


class AddCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name',
                  'email',
                  'phone',
                  'position',
                  'availability',
                  'main_skills',
                  'secondary_skills',
                  'showreel']

        labels = {'name': "Collaborator name",
                  'email': "Collaborator email",
                  'phone': "Collaborator phone",
                  'position': 'Collaborator position',
                  'availability': "Collaborator availability",
                  'main_skills': "Collaborator main skills",
                  'secondary_skills': "Collaborator secondary skills",
                  'showreel': "Collaborator showreel"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['position'].widget.attrs.update({'class': 'form-control'})
        self.fields['availability'].widget.attrs.update({'class': 'form-control'})
        self.fields['main_skills'].widget.attrs.update({'class': 'form-control'})
        self.fields['secondary_skills'].widget.attrs.update({'class': 'form-control'})
        self.fields['showreel'].widget.attrs.update({'class': 'form-control'})


class SearchCollaboratorForm(forms.Form):
    name = forms.CharField(
        label="Collaborator name",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label="Collaborator email",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = PhoneNumberField(
        label="Collaborator phone",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(
        label="Collaborator position",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    availability = forms.CharField(
        label="Collaborator availability",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_skills = forms.ModelChoiceField(
        label="Collaborator main skills",
        queryset=Skill.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    secondary_skills = forms.ModelChoiceField(
        label="Collaborator secondary skills",
        queryset=Skill.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    showreel = forms.URLField(
        label="Collaborator showreel",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

