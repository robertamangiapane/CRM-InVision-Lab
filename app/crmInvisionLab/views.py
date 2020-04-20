from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .edit_collaborator_helpers import edit_relation_skill_table
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
            collaborator_skill = CollaboratorSkill(main_skill="True",
                                                   collaborator=collaborator,
                                                   skill=skill)
            collaborator_skill.save()
            return redirect('/')
        else:
            raise ValidationError("Collaborator must have a name")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/add.html', {'collaborator_form': collaborator_form})


def view(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)
    skill = CollaboratorSkill.objects.get(collaborator=collaborator.id)

    return render(request, 'crmInvisionLab/collaborator.html', {'collaborator': collaborator,
                                                                'skill': skill.skill})


def edit(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)

    if request.method == "POST":
        collaborator_form = AddCollaboratorForm(request.POST, instance=collaborator)

        if collaborator_form.is_valid():
            collaborator_form.save()
            edit_relation_skill_table(collaborator, collaborator_form.data.__getitem__('main_skill'))
            return redirect('/collaborator/' + str(id_collaborator))
        else:
            raise ValidationError("Collaborator must have a name")
    else:
        collaborator_form = AddCollaboratorForm(instance=collaborator)

    return render(request, 'crmInvisionLab/edit.html', {'collaborator_form': collaborator_form,
                                                        'id_collaborator': id_collaborator})



