from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from langchain_openai import ChatOpenAI
from .models import ChatUser, ChatSession
from .serializer import ChatSessionSerializer, ChatUserSerializer
import uuid

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

class ChatSessionListCreateView(ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    permission_classes = [AllowAny]    

class ChatSessionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    permission_classes = [AllowAny]  

class ChatUserListCreateView(ListCreateAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserSerializer
    permission_classes = [AllowAny]    

class ChatUserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserSerializer
    permission_classes = [AllowAny]  

class ChatAPIView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):

        # 현재 대화가 첫번째이면 생성, 이미 있으면 업데이트

        chat_list = []

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

        chat_str = '항상 system 대화 문구는 정확한 사실만을 이야기 하며, 모르는것에 대해서는 정확히 모른다고 말하라.'

        session_name = request.data.get('session', None)
        
        try:
            gen_data = llm.invoke(chat_str)

            chat_list.append({'writer':'system', 'chatMessage':gen_data.content})

            if not ChatSession.is_valid_session(session_name):
                session_name = uuid.uuid4()

            obj, created = ChatSession.objects.get_or_created(
                session = session_name,
                content = '',
            )
            # 여기서 부터 만약 오브젝트 있을때 데이터가 어떻게 나오는지 확인

            # return {"answer": chat_list}
            return Response(status=status.HTTP_200_OK)
        except:
        # 예외처리
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)