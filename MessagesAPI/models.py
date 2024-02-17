from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MessageInfoItem(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    datetime_sent = models.DateTimeField(auto_now = True)
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sender')
    receivers = models.ManyToManyField(User, related_name= 'receivers')
    
    def __str__(self) -> str:
        return 'Message (title : "' + self.title +'") sent by ' + self.sender.username
    


