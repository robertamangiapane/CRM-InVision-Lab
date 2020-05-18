from ..models import Job
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .job_form import AddJobForm, SearchJobForm


class ProjectList(ListView):
    model = Job
    paginate_by = 50
    ordering = "name"

    # def get_queryset(self):
    #     project_search_form = SearchJobForm(self.request.GET)
    #     print(project_search_form.data['name'])
    #     sort_params = "collaborator_filter({})"
    #     # if project_search_form.is_valid() and self.request.GET:
    #     #     sort_params = ""
    #     #     # sort_params = collaborator_filter(search_form.cleaned_data)
    #     # return Job.objects.filter(**sort_params).order_by(self.ordering)
    #     return Job.objects.all()

    def get_context_data(self, **kwargs):
        if self.request.path == '/projects':
            projects = Job.objects.all()
        elif self.request.path == '/projects/old':
            projects = Job.objects.filter(ended=True)
        else:
            projects = Job.objects.filter(ended=False)

        context = {'projects': projects}
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
