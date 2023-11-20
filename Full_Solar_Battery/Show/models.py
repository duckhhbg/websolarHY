from django.db import models

# Create your models here.
class Manager_Model(models.Model):
    Jurisdiction_choices = [
        ("Giám sát", "Giám sát"),
        ("Quản trị", "Quản trị"),
        ("Điều khiển", "Điều khiển")
    ]
    Name = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Jurisdiction = models.CharField(choices=Jurisdiction_choices, max_length=20)