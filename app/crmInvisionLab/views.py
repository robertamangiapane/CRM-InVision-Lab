from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import CollaboratorSkill
from .models import Collaborator
from .models import Skill

from .collaborator_form import AddCollaboratorForm


def index(request):
    collaborators = Collaborator.objects.all()
    context = {'collaborators': collaborators}
    return render(request, 'crmInvisionLab/index.html', context)


def add(request):
    collaborator = Collaborator()

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator = collaborator_form.save()

            skill_name = collaborator_form.data.__getitem__('main_skill')

            # Exception
            # Type: DoesNotExist
            # Exception
            # Value:
            # Skill
            # matching
            # query
            # does
            # not exist.

            skill = Skill.objects.get(skill=skill_name)
            collaborator_skill = CollaboratorSkill(main_skill="True", collaborator=collaborator, skill=skill)
            collaborator_skill.save()
            return redirect('/')
        else:
            raise ValidationError("Collaborator must have a name")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/add.html', {'collaborator_form': collaborator_form})


def view(request, id_collaborator):
    collaborator = Collaborator.objects.get(pk=id_collaborator)
    context = {'collaborator': collaborator}

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

    return render(request, 'crmInvisionLab/edit.html', {'collaborator_form': collaborator_form})



