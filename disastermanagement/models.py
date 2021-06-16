from django.db import models

# Create your models here.
class Donors(models.Model):
    first_name=models.CharField(max_length=64, default="")
    last_name=models.CharField(max_length=64, default="")
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=64, default="")
    amount=models.PositiveBigIntegerField

    def __str__(self):
        return f"{self.first_name}  {self.last_name}   {self.username}"