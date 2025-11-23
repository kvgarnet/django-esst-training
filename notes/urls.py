from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),name="notes.detail"),
    path('popnotes', views.PopularNotesListView.as_view()),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
    # path('notes', views.list),
    # path('notes/<int:pk>', views.detail),
]
