from django.db import models

# Create your models here.
class Doctor(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='image')
    speciality = models.CharField(max_length=50)



class Appointment(models.Model):
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    number = models.CharField( max_length=50)