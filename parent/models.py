from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    reward = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Approval(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='task_images/', blank=True, null=True)
    

    def __str__(self):
        return self.title
    
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)