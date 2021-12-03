from django.db import models

from main.models import User

# Create your models here.

class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.DO_NOTHING)
    chat_identifier = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="file/", null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_time']

# class Files(models.Model):
#     file = models.FileField(upload_to='file/')