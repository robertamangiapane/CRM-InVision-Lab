from ..models import Job
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .job_form import AddJobForm


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
        status = "Not finished"
        # collaborators = ""
        if project.ended:
            status = "Project finished"

        context = {'project': project, 'status': status}
        return context
