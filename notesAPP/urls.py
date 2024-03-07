from django.urls import path
from . import views, utils

urlpatterns  = [
    path('notes', utils.getNotesList, name = 'notes'),
    path('notes/create', utils.createNote, name = 'create_note'),
    path('notes/<str:pk>', utils.getNoteDetail, name = 'note'),
    path('notes/update/<str:pk>', utils.updateNote, name = 'updatenote'),
    path('notes/delete/<str:pk>',utils.deleteNote, name = 'delete_note')
]