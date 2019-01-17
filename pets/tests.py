from django.test import TestCase

from volunteers.tests import create_sample_volunteer
from .models import Pet


def create_sample_pet():
    return Pet.objects.create(volunteer=create_sample_volunteer(),
                              name='test',
                              city='test',
                              race='test',
                              gender='test',
                              size='test',
                              age='1',
                              photo_main='fake.jpg')


class PetTests(TestCase):

    def test_pet_str(self):
        """Test the pet string representation"""
        pet = create_sample_pet()

        self.assertEqual(str(pet), pet.name)
