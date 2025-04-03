from django.db import models
from django.utils import timezone

class Trip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    photo = models.ImageField(upload_to='trips/')  # Изменили на ImageField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    is_canceled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.trip.title}"