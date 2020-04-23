from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Collaborator, Skill
from .collaborator_form import AddCollaboratorForm, SearchCollaboratorForm
from .filtering_helpers import *


def index(request):
    return render(request, 'crmInvisionLab/index.html')


def collaborators_index(request):
    collaborators = Collaborator.objects.order_by("name")
    search_form = SearchCollaboratorForm(request.GET)

    if search_form.is_valid():

        sort_params = collaborator_filter(search_form.cleaned_data)
        collaborators = Collaborator.objects.filter(**sort_params)

    context = {'collaborators': collaborators, 'search_form': search_form}
    return render(request, 'crmInvisionLab/collaborators_index.html', context)


def collaborator_add(request):
    collaborator = Collaborator()

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator = collaborator_form.save()
            return redirect('/collaborators/view/' + str(collaborator.id))
        else:
            raise ValidationError("Form is not valid")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/collaborator_add.html', {'collaborator_form': collaborator_form})


def collaborator_view(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)
    skill = collaborator.main_skills
    context = {'collaborator': collaborator, 'skill': skill}

    return render(request, 'crmInvisionLab/collaborator_view.html', context)


def collaborator_edit(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator_form.save()

            return redirect('/collaborators/view/' + str(id_collaborator))
        else:
            raise ValidationError("Collaborator must have a name")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/collaborator_edit.html', {'collaborator_form': collaborator_form,
                                                        'id_collaborator': id_collaborator})


def collaborator_delete(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)

    if request.method == "POST":
        collaborator.delete()
        return redirect('/collaborators')

    else:
        return render(request, 'crmInvisionLab/collaborators_index.html')


def skill_index(request):
    skills = Skill.objects.order_by("name")

    return render(request, 'crmInvisionLab/skills.html', {'skills': skills})


def skill_add(request):
    skill = Skill()
    if request.method == "POST":
        skill_name = request.POST["skill"]
        skill = Skill(name=skill_name)
        skill.save()

        return redirect('/skills')
    else:
        return render(request, 'crmInvisionLab/skills.html', {'skill': skill})


def skill_edit(request, id_skill):
    skill = Skill.objects.get(id=id_skill)

    if request.method == "POST":
        new_name = request.POST[skill.name]
        skill.name = new_name
        skill.save()

        return redirect('/skills')
    else:
        return render(request, 'crmInvisionLab/skills.html', {'skill': skill})


def skill_delete(request, id_skill):
    skill = Skill.objects.get(id=id_skill)

    if request.method == "POST":

        skill.delete()
        return redirect('/skills')
    else:
        return render(request, 'crmInvisionLab/skills.html', {'skill': skill})
