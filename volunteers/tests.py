from django.test import TestCase, Client

from .models import Volunteer


def create_sample_volunteer():
    return Volunteer.objects.create(name='Test',
                                    phone='555555555',
                                    email='test@test.com')


class VolunteerTests(TestCase):

    def test_volunteer_str(self):
        """Test the volunteer string representation"""
        volunteer = create_sample_volunteer()

        self.assertEqual(str(volunteer), volunteer.name)
