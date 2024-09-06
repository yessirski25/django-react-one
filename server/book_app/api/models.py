from django.db import models
from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):
    contactName = models.CharField(max_length=10)
    contactNumber = PhoneField(unique=True, blank=True)

    def __str__(self):
        return self.contactName