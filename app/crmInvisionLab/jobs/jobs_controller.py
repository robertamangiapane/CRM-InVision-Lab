from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .job_form import AddJobForm, SearchJobForm
from ..filtering_helpers import *


class ProjectList(ListView):
    model = Job
    paginate_by = 50
    ordering = "name"

    def get_queryset(self):
        project_search_form = SearchJobForm(self.request.GET)
        sort_params = get_filters({})
        if project_search_form.is_valid() and self.request.GET:
            sort_params = get_filters(project_search_form.cleaned_data)
        return Job.objects.filter(**sort_params).order_by(self.ordering)

    def get_context_data(self, **kwargs):
        project_search_form = SearchJobForm(self.request.GET)

        if self.request.path == '/projects/old':
            context = {'include_form': "False", 'projects': Job.objects.filter(ended=True)}

        elif self.request.path == '/projects/ongoing':
            context = {'include_form': "False", 'projects': Job.objects.filter(ended=False)}

        else:
            context = {'include_form': "True", 'project_search_form': project_search_form, 'projects': self.object_list}

        return context


class ProjectAdd(CreateView):
    model = Job

    def get_form(self, form_class=None):
        return super().get_form(AddJobForm)

    def form_valid(self, form):
        project = form.save()
        project.save()
        self.success_url = '/projects/view/' + str(project.id)
        return super().form_valid(form)


class ProjectView(DetailView):
    model = Job

    def get_context_data(self, **kwargs):
        project = self.object
        context = {'project': project}
        return context


class ProjectDelete(DeleteView):
    model = Job
    success_url = '/projects'


class ProjectUpdate(UpdateView):
    model = Job
    template_name_suffix = '_update_form'

    def get_form(self, form_class=None):
        return super().get_form(AddJobForm)

    def form_valid(self, form):
        self.object.save()
        self.success_url = '/projects/view/' + str(self.object.id)
        return super().form_valid(form)
