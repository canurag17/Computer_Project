from django.db import models

# Create your models here.

class book(models.Model):
    flying_from=models.CharField(max_length=50)
    flying_to=models.CharField(max_length=50)
    departing=models.DateField()
    returning=models.DateField()
    adults=models.IntegerField()
    children=models.IntegerField()
    travel_class=models.CharField(max_length=50)
    user_id=models.IntegerField()


class Flights(models.Model):
    Plane_ID=models.CharField(max_length=50)
    F=models.CharField(max_length=50)
    T=models.CharField(max_length=50)
    Departure_Time=models.CharField(max_length=50)
    Arrival_Time=models.CharField(max_length=50)
    Departure_City=models.CharField(max_length=50)
    Arrival_City=models.CharField(max_length=50)
    Price=models.IntegerField()
'''class Details(models.Model):
    Name=models.CharField(max_length=50)
    Person=models.CharField(max_length=5)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=100)'''
class History(models.Model):
    user_id=models.IntegerField()
    Plane_ID=models.CharField(max_length=50)
    F=models.CharField(max_length=50)
    T=models.CharField(max_length=50)
    departing=models.DateField()
    returning=models.DateField()
    adults=models.IntegerField()
    children=models.IntegerField()
    Departure_Time=models.CharField(max_length=50)
    Arrival_Time=models.CharField(max_length=50)
    Departure_City=models.CharField(max_length=50)
    Arrival_City=models.CharField(max_length=50)
    Price=models.IntegerField()
    


