from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    user_Type = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class registeredDomains(models.Model):
    company_name = models.CharField(max_length=30)
    company_Address = models.CharField(max_length=50)
    admin_officer = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)
    approved =  models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company_name} {self.admin_officer}"


class payments(models.Model):
    domain = models.CharField(max_length=30)
    PaymentReference = models.CharField(max_length=30)