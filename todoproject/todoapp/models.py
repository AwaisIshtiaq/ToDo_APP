from django.db import models

# Create your models here.
class Item(models.Model):
    task = models.CharField(max_length=150)
    task_description = models.TextField()

    def __str__(self):
        return self.task
    