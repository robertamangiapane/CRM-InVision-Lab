# Create your views here.
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Collaborator, Skill
from .collaborators.collaborator_form import AddCollaboratorForm, SearchCollaboratorForm
from .collaborators.collaborators_filtering_helpers import *
from .collaborators.collaborators_controller import *


def index(request):
    return render(request, 'crmInvisionLab/index.html')


# def collaborators_index(request):
#     collaborator_search_form = SearchCollaboratorForm(request.GET)
#     sort_params = collaborator_filter({})
#
#     if collaborator_search_form.is_valid() and request.GET:
#         sort_params = collaborator_filter(collaborator_search_form.cleaned_data)
#
#     collaborators = CollaboratorList().get_collaborators(**sort_params)
#
#     context = {'collaborators': collaborators, 'collaborator_search_form': collaborator_search_form}
#     return render(request, 'crmInvisionLab/collaborators_index.html', context)


# def collaborator_add(request):
#
#     if request.method == "POST":
#         collaborator_add_form = CollaboratorAdd().add_collaborator(request_post=request.POST)
#
#         if collaborator_add_form.is_valid():
#             collaborator = collaborator_add_form.save()
#
#             return redirect('/collaborators/view/' + str(collaborator.id))
#     else:
#         collaborator_add_form = CollaboratorAdd().add_collaborator()
#
#     return render(request, 'crmInvisionLab/collaborator_add.html', {'collaborator_add_form': collaborator_add_form})


def collaborator_view(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)
    main_skills = collaborator.main_skills
    secondary_skills = collaborator.secondary_skills
    # fields = collaborator._meta.get_all_field_names()
    context = {'collaborator': collaborator, 'main_skills': main_skills, 'secondary_skills': secondary_skills}

    return render(request, 'crmInvisionLab/collaborator_view.html', context)


def collaborator_edit(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator_form.save()

            return redirect('/collaborators/view/' + str(id_collaborator))
        else:
            raise ValidationError("Form is not valid")
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
        try:
            skill.save()

        except:
            messages.warning(request, 'Skill already exist')

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
        messages.warning(request, 'You deleted a skill')
        skill.delete()
        return redirect('/skills')
    else:
        return render(request, 'crmInvisionLab/skills.html', {'skill': skill})
