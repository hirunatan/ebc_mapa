from django.core.management.base import BaseCommand, CommandError
from cities.models import Subregion

class Command(BaseCommand):
    help = "Clean the spanish names of provinces"

    def handle(self, *args, **options):
        for subregion in Subregion.objects.filter(region__country__code="ES"):

            if subregion.name.startswith("Provincia de "):
                subregion.name = subregion.name[len("Provincia de "):]
            if subregion.name_std.startswith("Provincia de "):
                subregion.name_std = subregion.name_std[len("Provincia de "):]

            if subregion.name.startswith("Provincia da "):
                subregion.name = subregion.name[len("Provincia da "):]
            if subregion.name_std.startswith("Provincia da "):
                subregion.name_std = subregion.name_std[len("Provincia da "):]

            if subregion.name.startswith("Província de "):
                subregion.name = subregion.name[len("Província de "):]
            if subregion.name_std.startswith("Província de "):
                subregion.name_std = subregion.name_std[len("Província de "):]

            if subregion.name.startswith("Province of "):
                subregion.name = subregion.name[len("Province of "):]
            if subregion.name_std.startswith("Province of "):
                subregion.name_std = subregion.name_std[len("Province of "):]

            subregion.save()
            self.stdout.write(str(subregion))
