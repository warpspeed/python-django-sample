import datetime

from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_text
    def toggle_complete(self):
        self.is_complete = not self.is_complete