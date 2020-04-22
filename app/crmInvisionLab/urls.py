from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collaborators', views.collaborators_index, name="collaborators"),
    path('collaborators/add/collaborator', views.collaborator_add, name="add_collaborator"),
    path('collaborators/view/<str:id_collaborator>', views.collaborator_view, name='collaborator'),
    path('collaborators/edit/<str:id_collaborator>', views.collaborator_edit, name='edit_collaborator'),
    path('skills', views.skill_index, name="skills"),
    path('skills/add', views.skill_add, name="skills_add"),
    path('skills/delete/<str:id_skill>', views.skill_delete, name="skill_id_delete")
]