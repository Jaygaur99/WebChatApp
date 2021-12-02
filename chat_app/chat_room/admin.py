from django.contrib import admin
from django.core.files.base import File
from .models import Files, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(Files)