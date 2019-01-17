from django.test import TestCase, Client
from django.urls import reverse

from pets.tests import create_sample_pet
from .models import Contact


def create_sample_contact():
    return Contact.objects.create(pet=create_sample_pet(),
                                  name='test',
                                  email='test@test.com',
                                  phone='555555555',
                                  message='test')


class ContactTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contact_str(self):
        """Test the contact string representation"""
        contact = create_sample_contact()

        self.assertEqual(str(contact), contact.name)

    def test_contact_inquiry(self):
        """Test that contact inquiry was sent"""
        url = reverse('contact')
        pet = create_sample_pet()
        payload = {
            'pet': pet.id,
            'name': 'test',
            'email': 'test@test.com',
            'phone': '555555555',
            'message': 'test'
        }
        res = self.client.post(url, payload)
        exists = Contact.objects.filter(
            pet=payload['pet'],
            name=payload['name'],
            email=payload['email'],
            phone=payload['phone'],
            message=payload['message']
        ).exists()

        self.assertEqual(res.status_code, 302)
        self.assertTrue(exists)
