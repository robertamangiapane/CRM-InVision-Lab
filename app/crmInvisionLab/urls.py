from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collaborators', views.collaborators_index, name="collaborators"),
    path('collaborators/add/collaborator', views.collaborator_add, name="collaborator_add"),
    path('collaborators/view/<str:id_collaborator>', views.collaborator_view, name='collaborator_view'),
    path('collaborators/edit/<str:id_collaborator>', views.collaborator_edit, name='collaborator_edit'),
    path('skills', views.skill_index, name="skills"),
    path('skills/add', views.skill_add, name="skills_add"),
    # path('skills/edit', views.skill_edit, name="skills_edit"),
    path('skills/delete/<str:id_skill>', views.skill_delete, name="skill_id_delete")
]