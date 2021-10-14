from django.db import models

# Create your models here.
class signup(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pass1 = models.models.CharField(max_length=100)
    pass2 = models.models.CharField(max_length=100)