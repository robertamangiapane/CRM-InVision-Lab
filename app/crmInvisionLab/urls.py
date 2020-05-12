from django.urls import path
from . import views
from .collaborators.collaborators_controller import *
from .skills.skills_controller import *

urlpatterns = [
    path('', views.index, name='index'),
    path('collaborators', CollaboratorList.as_view(), name="collaborators"),
    path('collaborators/add/collaborator', CollaboratorAdd.as_view(), name="collaborator_add"),
    path('collaborators/view/<str:pk>', CollaboratorView.as_view(), name='collaborator_view'),
    path('collaborators/update/<str:pk>', CollaboratorUpdate.as_view(), name='collaborator_edit'),
    path('collaborators/delete/<str:pk>', CollaboratorDelete.as_view(), name='collaborator_delete'),
    path('skills', SkillAdd.as_view(), name="skills"),
    path('skills/update/<str:pk>', SkillUpdate.as_view(), name="skills_edit"),
    path('skills/delete/<str:pk>', SkillDelete.as_view(), name="skill_id_delete")
]