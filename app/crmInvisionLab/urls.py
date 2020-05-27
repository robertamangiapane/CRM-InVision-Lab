from django.urls import path
from . import views
from .collaborators.collaborators_controller import *
from .skills.skills_controller import *
from .jobs.jobs_controller import *
from .customers.customers_controller import *
from .competitors.competitors_controller import *

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', ProjectList.as_view(), name='projects'),
    path('projects/ongoing', ProjectList.as_view(), name='projects_ongoing'),
    path('projects/old', ProjectList.as_view(), name='projects_old'),
    path('projects/add/project', ProjectAdd.as_view(), name='project_add'),
    path('projects/view/<str:pk>', ProjectView.as_view(), name='project_view'),
    path('projects/update/<str:pk>', ProjectUpdate.as_view(), name='project_update'),
    path('projects/delete/<str:pk>', ProjectDelete.as_view(), name='project_delete'),
    path('clients', ClientList.as_view(), name='clients'),
    path('clients/add/client', ClientAdd.as_view(), name='client_add'),
    path('clients/view/<str:pk>', ClientView.as_view(), name='client_view'),
    path('clients/update/<str:pk>', ClientUpdate.as_view(), name='project_update'),
    path('clients/delete/<str:pk>', ClientDelete.as_view(), name='project_delete'),
    path('collaborators', CollaboratorList.as_view(), name='collaborators'),
    path('collaborators/add/collaborator', CollaboratorAdd.as_view(), name='collaborator_add'),
    path('collaborators/view/<str:pk>', CollaboratorView.as_view(), name='collaborator_view'),
    path('collaborators/update/<str:pk>', CollaboratorUpdate.as_view(), name='collaborator_edit'),
    path('collaborators/delete/<str:pk>', CollaboratorDelete.as_view(), name='collaborator_delete'),
    path('skills', SkillAdd.as_view(), name='skills'),
    path('skills/update/<str:pk>', SkillUpdate.as_view(), name='skills_edit'),
    path('skills/delete/<str:pk>', SkillDelete.as_view(), name='skill_delete'),
    path('competitors', CompetitorList.as_view(), name='competitors'),
    # path('competitors/add/competitor', CompetitorsAdd.as_view(), name='competitor_add'),
    # path('competitors/view/<str:pk>', CompetitorsView.as_view(), name='competitor_view'),
    # path('competitors/update/<str:pk>', CompetitorsUpdate.as_view(), name='competitor_edit'),
    # path('competitors/delete/<str:pk>', CompetitorsDelete.as_view(), name='competitor_delete')
]
