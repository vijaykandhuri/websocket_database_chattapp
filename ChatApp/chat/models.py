"""from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)"""


"""from mongoengine import Document, fields
from django.contrib.auth.models import User as MongoUser

class ChatMessage(Document):
    sender = fields.ReferenceField(MongoUser)
    receiver = fields.ReferenceField(MongoUser)
    message = fields.StringField()
    timestamp = fields.DateTimeField()
"""