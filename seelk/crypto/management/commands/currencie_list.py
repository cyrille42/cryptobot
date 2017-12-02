from django.core.management.base import BaseCommand
from crypto.task import Currencie_List

class Command(BaseCommand):

    def handle(self, *args, **options):
        Currencie_List()