from django.test import TestCase, Client
from django.urls import reverse, resolve
from appointment import path_name
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.contrib.auth import get_user_model
import unittest

class Tests(TestCase):

    def test_user_list_url_resolves(self):
        url = reverse('user-list')
        self.assertEqual(resolve(url).func, path_name.user_list)

    def test_user_detail_url_resolves(self):
        url = reverse('user-detail', args=[1])
        self.assertEqual(resolve(url).func, path_name.user_detail)

    def test_doctor_list_url_resolves(self):
        url = reverse('doctor_list')
        self.assertEqual(resolve(url).func, path_name.doctor_list)

    def test_doctor_detail_url_resolves(self):
        url = reverse('doctor_detail', args=[1])
        self.assertEqual(resolve(url).func, path_name.doctor_detail)

    def test_patient_list_url_resolves(self):
        url = reverse('patient_list')
        self.assertEqual(resolve(url).func, path_name.patient_list)

    def test_patient_detail_url_resolves(self):
        url = reverse('patient_detail', args=[1])
        self.assertEqual(resolve(url).func, path_name.patient_detail)

    def test_appointment_list_url_resolves(self):
        url = reverse('appointment_list')
        self.assertEqual(resolve(url).func, path_name.appointment_list)

    def test_appointment_detail_url_resolves(self):
        url = reverse('appointment_detail', args=[1])
        self.assertEqual(resolve(url).func, path_name.appointment_detail)

class MyTests(APITestCase):

    def setUp(self):
        # Erstelle einen User für den Arzt
        self.doctor_user = User.objects.create_user(
            username='testdoctor',
            password='testpassword'
        )
        
        # Erstelle einen Arzt
        self.doctor = Doctor.objects.create(
            user=self.doctor_user,
            speciality='Allgemeinmedizin',
            title='Dr.'
        )
        
        # Erstelle einen User für den Patienten
        self.patient_user = User.objects.create_user(
            username='testpatient',
            password='testpassword'
        )
        
        # Erstelle einen Patienten
        self.patient = Patient.objects.create(
            user=self.patient_user
        )
        
        # Erstelle einen Termin zwischen dem Arzt und dem Patienten
        self.appointment = Appointment.objects.create(
            title='Test Appointment',
            description='Test Description',
            patient=self.patient,
            doctor=self.doctor,
            date=datetime.now()
        )
        
    def test_list_doctors(self):
        self.client = Client()
        self.client.login(email=self.doctor_user.email, password=self.doctor_user.password)
        self.url = reverse(path_name.doctor_list)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)