from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList, related_name='items',
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text