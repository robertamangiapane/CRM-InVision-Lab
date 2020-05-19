from ..models import Collaborator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .collaborator_form import AddCollaboratorForm, SearchCollaboratorForm
from ..filtering_helpers import *


class CollaboratorList(ListView):
    model = Collaborator
    paginate_by = 50
    ordering = 'name'

    def get_queryset(self):
        collaborator_search_form = SearchCollaboratorForm(self.request.GET)
        sort_params = get_filters({})
        if collaborator_search_form.is_valid() and self.request.GET:
            sort_params = get_filters(collaborator_search_form.cleaned_data)
        return Collaborator.objects.filter(**sort_params).order_by(self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collaborator_search_form = SearchCollaboratorForm(self.request.GET)
        context['collaborator_search_form'] = collaborator_search_form
        return context


class CollaboratorAdd(CreateView):
    model = Collaborator

    def get_form(self, form_class=None):
        return super().get_form(AddCollaboratorForm)

    def form_valid(self, form):
        collaborator = form.save()
        collaborator.save()
        self.success_url = '/collaborators/view/' + str(collaborator.id)
        return super().form_valid(form)


class CollaboratorView(DetailView):
    model = Collaborator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collaborator'] = self.object
        return context


class CollaboratorDelete(DeleteView):
    model = Collaborator
    success_url = '/collaborators'


class CollaboratorUpdate(UpdateView):
    model = Collaborator
    template_name_suffix = '_update_form'

    def get_form(self, form_class=None):
        return super().get_form(AddCollaboratorForm)

    def form_valid(self, form):
        self.object.save()
        self.success_url = '/collaborators/view/' + str(self.object.id)
        return super().form_valid(form)

