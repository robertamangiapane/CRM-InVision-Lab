from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Collaborator

from .collaborator_form import AddCollaboratorForm


def index(request):
    collaborators = Collaborator.objects.all()
    # skills = []
    # for collaborator in collaborators:
    #     try:
    #         skill = CollaboratorSkill.objects.get(collaborator=collaborator.id).skill.skill
    #     except Exception:
    #         skill = ""
    #     skills.append(skill)

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
