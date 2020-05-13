from django import forms
from phonenumber_field.formfields import PhoneNumberField

from ..models import Collaborator, Skill, Job


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
                  'showreel',
                  'ongoing_projects',
                  'past_collaborations']

        labels = {'name': "Name",
                  'email': "Email",
                  'phone': "Phone",
                  'position': 'Position',
                  'availability': "When is available",
                  'main_skills': "Main skills",
                  'secondary_skills': "Secondary skills",
                  'showreel': "Showreel link",
                  'ongoing_projects': "Ongoing projects",
                  'past_collaborations': "Past collaborations"}


class SearchCollaboratorForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = PhoneNumberField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    availability = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_skills = forms.ModelChoiceField(
        queryset=Skill.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    secondary_skills = forms.ModelChoiceField(
        queryset=Skill.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    # showreel = forms.URLField(
    #     max_length=200,
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': 'form-control'}))
    ongoing_projects = forms.ModelChoiceField(
        queryset=Job.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    past_collaborations = forms.ModelChoiceField(
        queryset=Job.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
