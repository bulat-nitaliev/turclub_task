# apps/trips/tasks.py
from celery import shared_task
import time
from .models import Application

@shared_task
def create_application_async(data):
    # Искусственная задержка 5 секунд
    time.sleep(5)
    
    application = Application.objects.create(
        trip_id=data['trip_id'],
        full_name=data['full_name'],
        email=data['email'],
        phone=data['phone']
    )
    return application.id