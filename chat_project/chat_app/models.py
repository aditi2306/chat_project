# chat_app/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)

    class Meta:
        app_label = 'chat_app' 

class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = 'chat_app' 

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'chat_app' 
