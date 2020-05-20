from django import forms
from ..models import Job, Collaborator


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name',
                  'preview',
                  'link',
                  'collaborators',
                  'ended']

        labels = {'name': "Project name",
                  'preview': "Link to preview",
                  'link': "Link to final project",
                  'collaborators': "Collaborators involved",
                  'ended': 'Project completed'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['preview'].widget.attrs.update({'class': 'form-control'})
        self.fields['link'].widget.attrs.update({'class': 'form-control'})
        self.fields['collaborators'].widget.attrs.update({'class': 'form-control'})
        self.fields['ended'].widget.attrs.update({'class': 'form-control'})


class SearchJobForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    preview = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    link = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    collaborators = forms.ModelChoiceField(
        queryset=Collaborator.objects.order_by("name"),
        label="Collaborator involved",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
