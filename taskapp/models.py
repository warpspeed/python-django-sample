from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def toggle_complete(self):
        self.is_complete = not self.is_complete
