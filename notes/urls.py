from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
    path('popnotes', views.PopularNotesListView.as_view()),
    # path('notes', views.list),
    # path('notes/<int:pk>', views.detail),
]
