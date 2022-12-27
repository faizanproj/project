from django import forms   

from .models import *

class appointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name','city','age','date','time','number']
