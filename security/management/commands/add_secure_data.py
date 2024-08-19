# security/management/commands/add_secure_data.py
from django.core.management.base import BaseCommand
from security.models import SecureData
import random
import string


class Command(BaseCommand):
    help = 'Adds secure data to the database'

    def handle(self, *args, **kwargs):
        upi = generate_random_upi_id()
        print(upi)
        # Add your data creation logic here
        secure_data = SecureData.objects.create(
            user_id=random.randint(10000, 99999),
            bank_upi_encrypted=upi,
            pan_number_encrypted=generate_random_pan(),
            aadhaar_number_encrypted=generate_random_aadhaar()
        )

        self.stdout.write(self.style.SUCCESS(f'Secure data added: {secure_data}'))


def generate_random_upi_id(length=12):
    first_names = ['John', 'Jane', 'David', 'Emma', 'Michael', 'Sophia', 'Matthew', 'Olivia', 'Smith', 'Johnson',
                   'Williams', 'Brown', 'Jones', 'Garcia', 'Davis', 'Rodriguez']
    letters = string.ascii_lowercase
    end_point = ''.join(random.choice(letters) for _ in range(3))
    first_name = random.choice(first_names).lower()
    return f"{first_name}@{end_point}"


def generate_random_pan():
    # PAN number format: 5 letters followed by 4 digits and 1 letter (e.g., ABCDE1234F)
    letters = ''.join(random.choices(string.ascii_uppercase, k=5))
    digits = ''.join(random.choices(string.digits, k=4))
    last_letter = random.choice(string.ascii_uppercase)
    return f'{letters}{digits}{last_letter}'


def generate_random_aadhaar():
    # Aadhaar number format: 12 digits (e.g., 1234 5678 9012)
    return ' '.join(''.join(random.choices(string.digits, k=4)) for _ in range(3))
