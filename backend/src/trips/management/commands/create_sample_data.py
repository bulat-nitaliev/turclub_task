from django.core.management.base import BaseCommand
from faker import Faker
import random
from ...models import Trip, Application

class Command(BaseCommand):
    help = 'Creates sample trips and applications'

    def handle(self, *args, **options):
        fake = Faker()
        
        # Удаляем существующие данные
        Trip.objects.all().delete()
        lst = ['trips/Без названия.jpg', 'trips/ber.jpg', 'trips/fam.jpg',
         'trips/images.jpg','trips/ni.jpg','trips/see.jpg',]
        
        # Создаем 10 походов
        for i in lst:
            trip = Trip.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                start_date=fake.future_date(end_date=30),
                end_date=fake.future_date(end_date=60),
                photo=i
            )
            
            # Создаем 0-5 заявок для похода
            for _ in range(random.randint(0, 5)):
                Application.objects.create(
                    trip=trip,
                    full_name=fake.name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    is_canceled=fake.boolean(chance_of_getting_true=25)
                )
        
        self.stdout.write(self.style.SUCCESS('✅ Successfully created sample data'))