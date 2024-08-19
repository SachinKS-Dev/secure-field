from django.db import models
from core.fernet import _encrypt, _decrypt


class SecureData(models.Model):
    user_id = models.IntegerField(verbose_name='User ID')
    bank_upi_encrypted = models.BinaryField(verbose_name='Encrypted UPI id', blank=True, null=True)
    pan_number_encrypted = models.BinaryField(verbose_name='Encrypted PAN Number', blank=True, null=True)
    aadhaar_number_encrypted = models.BinaryField(verbose_name='Encrypted Aadhaar Number', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Encrypt PAN and Aadhaar numbers before saving
        self.pan_number_encrypted = _encrypt(self.pan_number_encrypted)
        self.aadhaar_number_encrypted = _encrypt(self.aadhaar_number_encrypted)
        self.bank_upi_encrypted = _encrypt(self.bank_upi_encrypted)
        super().save(*args, **kwargs)

    @property
    def masked_aadhaar(self):
        aadhaar_number = _decrypt(self.aadhaar_number_encrypted)
        return f'xxxxxxxx{aadhaar_number[-4:]}'

    @property
    def masked_pan(self):
        pan_number = _decrypt(self.pan_number_encrypted)
        return f'xxxxx{pan_number[-4:]}'

    @property
    def upi_id(self):
        return _decrypt(self.bank_upi_encrypted)

    def __str__(self):
        return f'SecureData #{self.id}'
