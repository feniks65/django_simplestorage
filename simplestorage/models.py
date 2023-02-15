#from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class File(models.Model):
    user = models.ForeignKey(User, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

