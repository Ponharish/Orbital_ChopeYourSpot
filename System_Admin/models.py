from django.db import models

# Create your models here.

class paymenthistorydump(models.Model):
    domain = models.CharField(max_length=30)
    PaymentReference = models.CharField(max_length=30)

class Message(models.Model):
    sender = models.CharField(max_length=30)
    senderdomain = models.CharField(max_length=30)

    receiver = models.CharField(max_length=30)
    receiverdomain = models.CharField(max_length=30)

    subject = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)