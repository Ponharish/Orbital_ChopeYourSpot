from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
    feedback_text = models.TextField()

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    Phone = models.IntegerField()
    subject = models.CharField(max_length=80)
    enquiry_text = models.TextField()