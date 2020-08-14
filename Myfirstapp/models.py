from django.db import models

class Carorder(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    carmodel=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=200)

    def __str__(self):
        return self.phoneno

