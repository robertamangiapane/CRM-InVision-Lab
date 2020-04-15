from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collaborator
from .collaborator_form import AddCollaboratorForm


def index(request):
    collaborators = Collaborator.objects.all()
    context = {'collaborators': collaborators}
    return render(request, 'crmInvisionLab/index.html', context)


def add(request):
    if request.method == "POST":
        form = AddCollaboratorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            raise ValidationError("Collaborator must have a name")

    return render(request, 'crmInvisionLab/add.html')


def view(request, id_collaborator):
    collaborator = Collaborator.objects.get(id=id_collaborator)
    context = {'collaborator': collaborator}

    return render(request, 'crmInvisionLab/collaborator.html', context)


def edit(request):
    return HttpResponse("Edit a selected collaborator")