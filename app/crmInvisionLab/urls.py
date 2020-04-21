from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/collaborator', views.add, name="add_collaborator"),
    path('collaborator/<str:id_collaborator>', views.view, name='collaborator'),
    path('edit/<str:id_collaborator>', views.edit, name='edit_collaborator'),
    path('skills/', views.skill_index, name="skills"),
    path('skills/add', views.skill_add, name="skills_add"),
    path('skills/delete/<str:id_skill>', views.skill_delete, name="skill_id_delete")
]