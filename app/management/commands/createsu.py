from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import dotenv
from pathlib import Path
import platform
import os
from django.db.utils import IntegrityError


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            
            if "amzn" not in platform.platform():
                dotenv.load_dotenv(os.path.join(BASE_DIR, ".env"))
            
            try:
                User.objects.create_superuser(os.environ["SU_USERNAME"], os.environ["SU_EMAIL"], os.environ["SU_PASSWORD"])
            except IntegrityError:
                print("Username already created.")