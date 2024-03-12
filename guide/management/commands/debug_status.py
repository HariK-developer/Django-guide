from django.core.management.base import BaseCommand
from django.conf import settings



class Command(BaseCommand):
    help = "Show the debug status of the application"
    
    def handle(self,*args, **options):
        self.stdout.write(f"DEBUG is {settings.DEBUG}")