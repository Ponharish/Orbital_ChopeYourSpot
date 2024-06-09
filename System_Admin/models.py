from django.db import models

# Create your models here.

class paymenthistorydump(models.Model):
    domain = models.CharField(max_length=30)
    PaymentReference = models.CharField(max_length=30)