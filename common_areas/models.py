from django.db import models

# Create your models here.

class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=4)
    longitud = models.DecimalField(max_digits=6, decimal_places=4)    
    def __str__(self):
        return f"Lat:{self.latitude}  Long{self.longitud}"
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    first_last_name = models.CharField(max_length=20, null=True, blank=True)
    second_last_name = models.CharField(max_length=20, null=True,blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.first_last_name} {self.second_last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.first_last_name} {self.second_last_name}"


class Habitational_Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"


class Home(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    number = models.IntegerField(null=True)
    habitational_area = models.ForeignKey(
        Habitational_Area,
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return f"{self.habitational_area.name}: {self.number} - {self.contact_person}"

class Common_Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    name: str = models.CharField(max_length=120)
    availability_starts = models.CharField(max_length=5, null=True, blank=True)
    availability_stop = models.CharField(max_length=5, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    habitational_area = models.ForeignKey(
        Habitational_Area,
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f"{self.habitational_area.name}: {self.name}"
    
