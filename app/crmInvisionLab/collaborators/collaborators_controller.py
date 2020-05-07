from ..models import Collaborator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .collaborator_form import AddCollaboratorForm, SearchCollaboratorForm


class CollaboratorList(ListView):
    model = Collaborator
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collaborator_search_form = SearchCollaboratorForm()
        context['collaborator_search_form'] = collaborator_search_form
        # collaborators = Collaborator.objects.filter(**sort_params)
        return context


class CollaboratorAdd(CreateView):
    model = Collaborator
    fields = AddCollaboratorForm.Meta.fields

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control'})
        form.fields['email'].widget.attrs.update({'class': 'form-control'})
        form.fields['phone'].widget.attrs.update({'class': 'form-control'})
        form.fields['position'].widget.attrs.update({'class': 'form-control'})
        form.fields['availability'].widget.attrs.update({'class': 'form-control'})
        form.fields['main_skills'].widget.attrs.update({'class': 'form-control'})
        form.fields['secondary_skills'].widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        collaborator = form.save()
        collaborator.save()
        self.success_url = '/collaborators/view/' + str(collaborator.id)
        return super().form_valid(form)


class CollaboratorView(DetailView):
    model = Collaborator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # collaborator = Collaborator.objects.get(id=id_collaborator)
        # context['now'] = timezone.now()
        return context

