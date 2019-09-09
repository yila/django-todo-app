from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    # After adding the inheritance, run the following command:
    # python manage.py makemigrations
    description = models.TextField()
    pass
