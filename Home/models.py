from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.CharField(max_length=244)
    desc = models.TextField()

    def __str__(self):
        return self.name