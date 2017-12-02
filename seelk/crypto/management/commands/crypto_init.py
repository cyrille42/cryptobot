from django.core.management.base    import BaseCommand
from crypto.models                  import Rule

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            Rule.objects.get(currencie="USD")
            print("USD Rule already exist")
        except:
            Rule.objects.create(currencie="USD", value_min=10000, value_max=14000)
            print("USD Rule created")