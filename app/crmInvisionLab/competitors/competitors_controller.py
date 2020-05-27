from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .competitor_form import AddCompetitorForm, SearchCompetitorForm
from ..filtering_helpers import *


class CompetitorList(ListView):
    model = Competitor
    paginate_by = 50
    ordering = 'name'

    def get_queryset(self):
        competitor_search_form = SearchCompetitorForm(self.request.GET)
        sort_params = get_filters({})
        if competitor_search_form.is_valid() and self.request.GET:
            sort_params = get_filters(competitor_search_form.cleaned_data)
        return Competitor.objects.filter(**sort_params).order_by(self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        competitor_search_form = SearchCompetitorForm(self.request.GET)
        context['competitor_search_form'] = competitor_search_form
        return context


class CompetitorAdd(CreateView):
    model = Competitor

    def get_form(self, form_class=None):
        return super().get_form(AddCompetitorForm)

    def form_valid(self, form):
        competitor = form.save()
        competitor.save()
        self.success_url = '/competitors/view/' + str(competitor.id)
        return super().form_valid(form)


class CompetitorView(DetailView):
    model = Competitor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competitor'] = self.object
        return context


class CompetitorDelete(DeleteView):
    model = Competitor
    success_url = '/competitors'


class CompetitorUpdate(UpdateView):
    model = Competitor
    template_name_suffix = '_update_form'

    def get_form(self, form_class=None):
        return super().get_form(AddCompetitorForm)

    def form_valid(self, form):
        self.object.save()
        self.success_url = '/competitors/view/' + str(self.object.id)
        return super().form_valid(form)
