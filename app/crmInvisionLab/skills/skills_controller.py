from ..models import Skill
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class SkillAdd(CreateView):
    template_name_suffix = '_list'
    model = Skill
    fields = ['name']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def form_valid(self, form):
        if form.is_valid():
            skill = form.save()
            skill.save()
            self.success_url = '/skills'

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skills = Skill.objects.order_by("name")
        context['skills'] = skills
        return context


class SkillDelete(DeleteView):
    model = Skill
    success_url = '/skills'


class SkillUpdate(UpdateView):
    template_name_suffix = '_list'
    model = Skill
    fields = ["name"]
    success_url = '/skills'




