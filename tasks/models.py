from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=150)
    descrition = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank= True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.user.username