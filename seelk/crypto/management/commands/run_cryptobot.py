from django.core.management.base import BaseCommand
from crypto.task import Cryptobot

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('currencie_name', type=str)

    def handle(self, *args, **options):
        Cryptobot(options['currencie_name'])