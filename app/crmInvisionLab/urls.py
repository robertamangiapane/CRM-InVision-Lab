from django.urls import path
from . import views
from .collaborators.collaborators_controller import *

urlpatterns = [
    path('', views.index, name='index'),
    path('collaborators', CollaboratorList.as_view(), name="collaborators"),
    path('collaborators/add/collaborator', CollaboratorAdd.as_view(), name="collaborator_add"),
    path('collaborators/view/<str:pk>', CollaboratorView.as_view(), name='collaborator_view'),
    path('collaborators/edit/<str:id_collaborator>', views.collaborator_edit, name='collaborator_edit'),
    path('collaborators/delete/<str:id_collaborator>', views.collaborator_delete, name='collaborator_delete'),
    path('skills', views.skill_index, name="skills"),
    path('skills/add', views.skill_add, name="skills_add"),
    path('skills/edit/<str:id_skill>', views.skill_edit, name="skills_edit"),
    path('skills/delete/<str:id_skill>', views.skill_delete, name="skill_id_delete")
]