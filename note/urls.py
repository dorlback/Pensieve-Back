from django.urls import path
from note.views import NoteListCreateView, NoteRetrieveUpdateDestroyView, TagListCreateView, TagRetrieveUpdateDestroyView, NoteUserListCreateView, NoteUserRetrieveUpdateDestroyView

urlpatterns = [
    # 노트
    path("notes", NoteListCreateView.as_view(), name="note-list-create"),
    path("notes/<int:pk>", NoteRetrieveUpdateDestroyView.as_view(), name='note-detail-update-destroy'),

    path("tags", TagListCreateView.as_view(), name="tag-list-create"),
    path("tags/<int:pk>", TagRetrieveUpdateDestroyView.as_view(), name='tag-detail-update-destroy'),

    path("noteusers", NoteUserListCreateView.as_view(), name="noteuser-list-create"),
    path("noteusers/<int:pk>", NoteUserRetrieveUpdateDestroyView.as_view(), name='noteuser-detail-update-destroy'),
]