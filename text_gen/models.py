from django.db import models
from user.models import User
import uuid

# Create your models here.
class ChatSession(models.Model):
    session_name = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    content = models.JSONField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_session'

    @classmethod
    def is_valid_session(cls, session_name):
        return cls.objects.filter(session_name=session_name).exists()

class ChatUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_user'
        unique_together = ('user', 'chat_session')