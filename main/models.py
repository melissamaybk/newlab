from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=100)

    def __str__(self):
	    return self.name