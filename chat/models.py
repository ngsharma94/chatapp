from django.db import models
from account.models import User

# Create your models here.

class ChatCoversationUser(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)

class ChatConversation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    USER_TYPE_CHOICES = [
        ('S', 'Sender'),
        ('R', 'Receiver')
    ]
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    
    