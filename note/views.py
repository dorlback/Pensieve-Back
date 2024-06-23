from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from note.models import Tag, Note, NoteUser
from note.serializer import TagSerializer, NoteSerializer, NoteUserSerializer

class NoteListCreateView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

class TagListCreateView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class TagRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class NoteUserListCreateView(ListCreateAPIView):
    queryset = NoteUser.objects.all()
    serializer_class = NoteUserSerializer
    permission_classes = [AllowAny]

class NoteUserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = NoteUser.objects.all()
    serializer_class = NoteUserSerializer
    permission_classes = [AllowAny]