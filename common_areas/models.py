from django.db import models

# Create your models here.

class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=2)
    longitud = models.DecimalField(max_digits=6, decimal_places=2)    

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    first_last_name = models.CharField(max_length=20)
    second_last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)


class Habitational_Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Home(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    habitational_area = models.ForeignKey(
        Habitational_Area,
        on_delete=models.PROTECT,
        null=True
    )

class Common_Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    name: str = models.CharField(max_length=120)
    availability_starts = models.CharField(max_length=5)
    availability_stop = models.CharField(max_length=5)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    habitational_area = models.ForeignKey(
        Habitational_Area,
        on_delete=models.CASCADE,
        null=True
    )
