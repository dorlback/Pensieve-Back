from django.urls import path
from text_gen.views import ChatAPIView, ChatSessionListCreateView, ChatSessionRetrieveUpdateDestroyView, ChatUserListCreateView, ChatUserRetrieveUpdateDestroyView
urlpatterns = [
    # 챗 세션
    path("chat_session", ChatSessionListCreateView.as_view(), name="chat-session-list-create"),
    path("chat_session/<int:pk>", ChatSessionRetrieveUpdateDestroyView.as_view(), name="chat-session-detail-update-destroy"),
    # 챗 유저
    path("chat_user", ChatUserListCreateView.as_view(), name="chat-user-list-create"),
    path("chat_user/<int:pk>", ChatUserRetrieveUpdateDestroyView.as_view(), name="chat-user-detail-update-destroy"),
    # 테스트 코드
    path("chat_test", ChatAPIView.as_view(), name="generate-text"),
]

