from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
    user = models.CharField('FISH', max_length=255)
    task = models.CharField('Mavzu', max_length=255)
    file = models.FileField('Video', upload_to='db_files')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
