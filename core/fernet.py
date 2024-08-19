from cryptography.fernet import Fernet

from secure_field import settings


def _encrypt(value):
    cipher_suite = Fernet(settings.ENCRYPTION_KEY)
    return cipher_suite.encrypt(value.encode())


def _decrypt(value):
    cipher_suite = Fernet(settings.ENCRYPTION_KEY)
    return cipher_suite.decrypt(value).decode()
