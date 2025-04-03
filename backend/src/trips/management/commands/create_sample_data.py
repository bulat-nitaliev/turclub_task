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
        
        # Создаем 10 походов
        for i in range(1, 11):
            trip = Trip.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                start_date=fake.future_date(end_date=30),
                end_date=fake.future_date(end_date=60),
                photo=f'https://picsum.photos/seed/{i}/600/400'
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