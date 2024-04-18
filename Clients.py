from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp1.models import Client


class Command(BaseCommand):
    help = "Creates clients in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        client = Client(
            name="Monstr",
            email="Monstr@Monstr.com",
            phone_number="+79658874679",
            address="Kolomna, square Lenin",
            registration_date=date(year=2021, month=4, day=1),
        )
        client.save()
        self.stdout.write(f"{client}")