from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    ACTIVITY_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
    ]

    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km
    calories_burned = models.IntegerField()
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity_type} - {self.user.username}"