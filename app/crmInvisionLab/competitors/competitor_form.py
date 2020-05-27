from django import forms
from ..models import Competitor


class AddCompetitorForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['name',
                  'website',
                  'position',
                  'showreel']

        labels = {'name': "Competitor Name",
                  'website': "Competitor website",
                  'position': 'Competitor position',
                  'showreel': "Competitor last showreel"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['website'].widget.attrs.update({'class': 'form-control'})
        self.fields['position'].widget.attrs.update({'class': 'form-control'})
        self.fields['showreel'].widget.attrs.update({'class': 'form-control'})


class SearchCompetitorForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    showreel = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))


