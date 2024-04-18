from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp1.models import Product


class Command(BaseCommand):
    help = "Creates products in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        product = Product(
            title="telephone",
            description="Good telephone",
            price=17000,
            qnt=2,
            creation_date=date(year=2024, month=7, day=25),
        )
        product.save()
        self.stdout.write(f"{product}")