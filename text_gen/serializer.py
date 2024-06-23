from rest_framework import serializers
from .models import ChatSession, ChatUser
from user.models import User
from user.serializer import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.urls import reverse
from langchain_openai import ChatOpenAI

class ChatSessionSerializer(WritableNestedModelSerializer, serializers.Serializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = ChatSession
        fields = ['pk', 'users', 'session', 'content', 'created_date']

class ChatUserSerializer(WritableNestedModelSerializer, serializers.Serializer):
    user = UserSerializer()
    chat_session = ChatSessionSerializer()

    class Meta:
        model = ChatUser
        fields = ['pk', 'user', 'chat_session', 'joined_at']

class ChatSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = ChatSession
        fields = ['pk', 'users', 'session', 'content', 'created_date']

    def update(self, instance, validated_data):
        instance.input_text = validated_data.get('input_text', instance.input_text)
        # LLM 모델 호출 로직 추가
        instance.generated_text = self.generate_text(instance.input_text)
        instance.save()
        return instance
    
    # def generate_text(self, input_text):
    #     # 이미 있는 데이터와, 새로 입력된 내용, 생성된 내용 합쳐서 다시 저장.
    #     chat_list = []

    #     llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

    #     chat_str = '항상 system 대화 문구는 한국인이 러시아 어를 흉내 내듯이 말 끝에 시바 를 붙여서 사용 하도록 하라. 존대말 하지 말고 무조건 반말을 사용 하여라. 농담 농도를 30프로 섞어서 친근하게 대화 하도록 하라.'

    #     gen_data = llm.invoke(chat_str)

    #     chat_list.append({'writer':'system', 'chatMessage':gen_data.content})

    #     return {"answer": chat_list}

        # import openai
        # openai.api_key = 'your-openai-api-key'

        # response = openai.Completion.create(
        #     engine="davinci-codex",
        #     prompt=input_text,
        #     max_tokens=150
        # )

        # generated_text = response.choices[0].text.strip()
        # return generated_text