from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1 
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404

def change_visibility_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public 
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

    #overwrite the form_valid method to associate form object with request's login user info to fix not null constraint of notes model 
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"
    #overwrite get_queryset of ListView class to query only notes belong to user , see ccbv.co,uk for get_queryset
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(likes__gte=1)
    login_url = "/admin"
