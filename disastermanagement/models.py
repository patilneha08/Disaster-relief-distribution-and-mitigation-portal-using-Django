from django.db import models

# Create your models here.


class Donor(models.Model):
    first_name = models.CharField(max_length=64, default="")
    last_name = models.CharField(max_length=64, default="")
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=64, default="")
    amount = models.BigIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}  {self.email}"


class Volunteer(models.Model):
    first_name = models.CharField(max_length=64, default="")
    last_name = models.CharField(max_length=64, default="")
    phone = models.BigIntegerField()
    altphone = models.BigIntegerField()
    email = models.EmailField(max_length=64, default="")
    gender = models.CharField(max_length=64, default="")
    age = models.IntegerField(default="")
    address = models.CharField(max_length=200, default="")
    bloodgroup = models.CharField(max_length=64, default="")
    aadhar = models.CharField(max_length=64, default="")
    service = models.CharField(max_length=64, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class NGO(models.Model):
    name = models.CharField(max_length=64, default="")
    address = models.CharField(max_length=200, default="")
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=64, default="")

    def __str__(self):
        return f"{self.name} NGO"
