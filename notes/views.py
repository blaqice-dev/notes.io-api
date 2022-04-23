from rest_framework import generics, permissions

from notes.serializers import NoteSerializer
from notes.models import Note


class ListCreateNoteAPIView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (permissions.AllowAny, )


class RetrieveUpdateDestroyNoteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (permissions.AllowAny, )
    lookup_field = 'id'
