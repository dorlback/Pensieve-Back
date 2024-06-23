from django.db import models
from user import models as user_models

class PermissionChoices(models.IntegerChoices):
    VIEWER = 1, 'Viewer'
    EDITOR = 2, 'Editor'
    OWNER = 3, 'Owner'



class Note(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notes'

class Tag(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="note_id")
    title = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tags'

class NoteUser(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=PermissionChoices.choices, default=PermissionChoices.OWNER)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'note_users'
        unique_together = (('user', 'note'),)