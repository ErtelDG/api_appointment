from django.contrib import admin
from appointment.models import Patient, Doctor, Appointment
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)