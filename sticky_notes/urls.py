from django.urls import path
from . import views


app_name = 'sticky_notes'


urlpatterns = [
path('', views.NoteListView.as_view(), name='note-list'),
path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
path('note/new/', views.NoteCreateView.as_view(), name='note-create'),
path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note-update'),
path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),
]