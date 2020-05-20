from django import forms
from phonenumber_field.formfields import PhoneNumberField
from ..models import Customer, Job


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name',
                  'email',
                  'phone',
                  'position',
                  'contact',
                  'contact_phone',
                  'contact_email',
                  'ongoing_projects',
                  'old_projects']

        labels = {'name': "Name",
                  'email': "Email",
                  'phone': "Phone",
                  'position': 'Position',
                  'contact': "Company contact person",
                  'contact_phone': "Contact phone",
                  'contact_email': "Contact email",
                  'ongoing_projects': "Ongoing projects",
                  'old_projects': "Old projects"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['position'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['ongoing_projects'].widget.attrs.update({'class': 'form-control'})
        self.fields['old_projects'].widget.attrs.update({'class': 'form-control'})


class SearchClientForm(forms.Form):
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
    contact = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_phone = PhoneNumberField(
        max_length=200,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    contact_email = forms.EmailField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    ongoing_projects = forms.ModelChoiceField(
        queryset=Job.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    old_projects = forms.ModelChoiceField(
        queryset=Job.objects.order_by("name"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
