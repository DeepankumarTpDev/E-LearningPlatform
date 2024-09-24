from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
# Create your models here.
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=False)
    course = models.ForeignKey(Course, related_name='messages', on_delete=models.CASCADE)
    isdeleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.content
