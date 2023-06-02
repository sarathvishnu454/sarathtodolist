from django.db import models

# Create your models here.
class todolist(models.Model):
    name=models.CharField(max_length=150)
    date=models.DateTimeField()
    priority=models.CharField(max_length=300)

    def __str__(self):
        return self.name


