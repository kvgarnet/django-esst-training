from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView,CreateView, UpdateView
from .models import Notes
from .forms import NotesForm

# Create your views here.

# use class-based view to replace function-based view 
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    #template_name is optional, since 'notes_list.html' is the name standard of ListView Class required, 
    # if it is a different template file name, we need to use 'template_name'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gte=1)

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title','text']
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


#below function-based views are replaced by class-based view
'''
def list(request):
    all_notes = Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes': all_notes})

def detail(request,pk):
    try: 
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request,'notes/notes_detail.html',{'note': note})
'''
