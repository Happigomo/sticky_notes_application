from django.views.generic import (
ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'sticky_notes/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'sticky_notes/note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'sticky_notes/note_form.html'


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'sticky_notes/note_form.html'


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'sticky_notes/note_confirm_delete.html'
    success_url = reverse_lazy('sticky_notes:note-list')
