from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def test_string_representation(self):
        n = Note.objects.create(title="Hello", content="World")
        self.assertEqual(str(n), "Hello")

    def test_created_and_updated_fields(self):
        n = Note.objects.create(title="A", content="B")
        self.assertIsNotNone(n.created_at)
        self.assertIsNotNone(n.updated_at)

class NoteViewTests(TestCase):
    def setUp(self):
        # create a note to use in tests
        self.note = Note.objects.create(title="Test note", content="Test content")

    def test_note_list_view(self):
        url = reverse('sticky_notes:note-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Test note")
        # context contains notes
        self.assertIn('notes', resp.context)

    def test_note_detail_view(self):
        url = reverse('sticky_notes:note-detail', args=[self.note.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Test content")

    def test_note_create_view(self):
        url = reverse('sticky_notes:note-create')
        resp_get = self.client.get(url)
        self.assertEqual(resp_get.status_code, 200)
        # POST create
        resp = self.client.post(url, {'title': 'New note', 'content': 'New content'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Note.objects.filter(title='New note').exists())

    def test_note_update_view(self):
        url = reverse('sticky_notes:note-update', args=[self.note.pk])
        resp_get = self.client.get(url)
        self.assertEqual(resp_get.status_code, 200)
        resp = self.client.post(url, {'title': 'Changed', 'content': 'Changed content'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Changed')

    def test_note_delete_view(self):
        url = reverse('sticky_notes:note-delete', args=[self.note.pk])
        resp_get = self.client.get(url)
        self.assertEqual(resp_get.status_code, 200)
        resp = self.client.post(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())

class NoteFormValidationTest(TestCase):
    def test_create_requires_title(self):
        url = reverse('sticky_notes:note-create')
        resp = self.client.post(url, {'title': '', 'content': 'No title'}, follow=True)
        # Should return form with errors (status 200) and not create the note
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Note.objects.filter(content='No title').exists())
        self.assertContains(resp, 'This field is required', status_code=200)

