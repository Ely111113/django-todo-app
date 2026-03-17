from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField(default=now)

    def __str__(self):
        return self.title