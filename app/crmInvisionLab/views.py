from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Collaborator, Skill

from .collaborator_form import AddCollaboratorForm


def index(request):
    collaborators = Collaborator.objects.order_by("name")
    context = {'collaborators': collaborators}

    return render(request, 'crmInvisionLab/index.html', context)


def add(request):
    collaborator = Collaborator()

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator = collaborator_form.save()
            return redirect('/collaborator/' + str(collaborator.id))
        else:
            raise ValidationError("Form is not valid")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/add.html', {'collaborator_form': collaborator_form})


def view(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)
    skill = collaborator.main_skills
    context = {'collaborator': collaborator, 'skill': skill}

    return render(request, 'crmInvisionLab/collaborator.html', context)


def edit(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator_form.save()

            return redirect('/collaborator/' + str(id_collaborator))
        else:
            raise ValidationError("Collaborator must have a name")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/edit.html', {'collaborator_form': collaborator_form,
                                                        'id_collaborator': id_collaborator})


def skill_index(request):
    skills = Skill.objects.order_by("name")

    return render(request, 'crmInvisionLab/skills.html', {'skills': skills})


def skill_add(request):
    skill = Skill()
    if request.method == "POST":
        skill_name = request.POST["skill"]
        print(skill_name)

        skill = Skill(name=skill_name)
        skill.save()
        print(skill.name)

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
