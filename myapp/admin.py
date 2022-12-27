from django.contrib import admin
from .models import Doctor,Appointment
# Register your models here.


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["speciality", "img", "name"][::-1]

    


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["number", "time", "date", "city", "age", "name"][::-1]


