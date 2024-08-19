# security/management/commands/get_secure_data.py

from django.core.management.base import BaseCommand
from security.models import SecureData
from django.conf import settings
from cryptography.fernet import Fernet

class Command(BaseCommand):
    help = 'Retrieves and decrypts secure data from the database'

    def handle(self, *args, **kwargs):
        # Retrieve all SecureData instances
        secure_data_objects = SecureData.objects.all()


        # Retrieve encryption key from settings
        encryption_key = settings.ENCRYPTION_KEY
        cipher_suite = Fernet(encryption_key)

        # Decrypt and display data
        for secure_data in secure_data_objects:
            try:
                pan = secure_data.masked_pan
                aadhaar = secure_data.masked_aadhaar

                self.stdout.write(self.style.SUCCESS(f" #{secure_data.id}: USER='{secure_data.user_id}', PAN='{pan}', Aadhaar='{aadhaar}', UPI='{secure_data.upi_id}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error decrypting data for SecureData #{secure_data.id}: {str(e)}"))
