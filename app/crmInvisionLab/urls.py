from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/collaborator', views.add, name="add_collaborator"),
    path('collaborator/<str:id_collaborator>', views.view, name='collaborator'),
    path('edit/', views.edit, name='edit')
]