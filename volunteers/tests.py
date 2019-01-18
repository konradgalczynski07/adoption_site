from django.test import TestCase, Client
from django.urls import reverse

from .models import Volunteer


def create_sample_volunteer():
    return Volunteer.objects.create(name='Test',
                                    photo='fake.jpg',
                                    phone='555555555',
                                    email='test@test.com')


class VolunteerTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_volunteer_str(self):
        """Test the volunteer string representation"""
        volunteer = create_sample_volunteer()

        self.assertEqual(str(volunteer), volunteer.name)

    def test_volunteer_listed(self):
        """Test that volunteers are listed on about page"""
        url = reverse('about')
        volunteer = create_sample_volunteer()
        res = self.client.get(url)

        self.assertContains(res, volunteer.name)
        self.assertContains(res, volunteer.phone)
        self.assertContains(res, volunteer.email)
