from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator,MaxLengthValidator

def only_int(value):
    if value.isdigit() == False:
        raise ValidationError('ID contains characters')

class Klient(models.Model):
    nazwa = models.CharField(max_length=200)
    nip = models.CharField(validators=[only_int,MinLengthValidator(10)],max_length=10)
    adres = models.CharField(max_length=100)
    miejscowosc = models.CharField(max_length=30)
    wojewodztwo = models.CharField(max_length=30)
    telefon = models.CharField(validators=[only_int,MinLengthValidator(9)],max_length=9)
    grupa = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

