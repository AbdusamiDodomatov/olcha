from django.core.management.base import BaseCommand
from products.models import Product, Category
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Генерирует случайные продукты'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество продуктов для создания')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        categories = list(Category.objects.all())
        if not categories:
            for _ in range(5):
                categories.append(Category.objects.create(
                    name=fake.word().capitalize(),
                    description=fake.text(max_nb_chars=50)
                ))

        for _ in range(total):
            Product.objects.create(
                name=fake.unique.word().capitalize(),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(10, 5000), 2),
                stock=random.randint(0, 100),
                category=random.choice(categories)
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Успешно создано {total} продуктов'))
