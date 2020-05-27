from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .customer_form import AddClientForm, SearchClientForm
from ..filtering_helpers import *


class ClientList(ListView):
    model = Customer
    paginate_by = 50
    ordering = 'name'

    def get_queryset(self):
        client_search_form = SearchClientForm(self.request.GET)
        sort_params = get_filters({})
        if client_search_form.is_valid() and self.request.GET:
            sort_params = get_filters(client_search_form.cleaned_data)
        return Customer.objects.filter(**sort_params).order_by(self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_search_form = SearchClientForm(self.request.GET)
        context['client_search_form'] = client_search_form
        return context


class ClientAdd(CreateView):
    model = Customer

    def get_form(self, form_class=None):
        return super().get_form(AddClientForm)

    def form_valid(self, form):
        client = form.save()
        client.save()
        self.success_url = '/clients/view/' + str(client.id)
        return super().form_valid(form)


class ClientView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.object
        return context


class ClientDelete(DeleteView):
    model = Customer
    success_url = '/clients'


class ClientUpdate(UpdateView):
    model = Customer
    template_name_suffix = '_update_form'

    def get_form(self, form_class=None):
        return super().get_form(AddClientForm)

    def form_valid(self, form):
        self.object.save()
        self.success_url = '/clients/view/' + str(self.object.id)
        return super().form_valid(form)
