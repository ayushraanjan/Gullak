from django.db import models
from django.contrib.auth.models import User

class ChildwalletBalance (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)