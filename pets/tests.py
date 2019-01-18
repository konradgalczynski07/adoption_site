from django.test import TestCase, Client
from django.urls import reverse

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

    def setUp(self):
        self.client = Client()

    def test_pet_str(self):
        """Test the pet string representation"""
        pet = create_sample_pet()

        self.assertEqual(str(pet), pet.name)

    def test_pet_listed_index(self):
        """Test that pets are listed on index page"""
        url = reverse('index')
        pet = create_sample_pet()
        res = self.client.get(url)

        self.assertContains(res, pet.name)
        self.assertContains(res, pet.city)

    def test_pet_listed_pets(self):
        """Test that pets are listed on pets page"""
        url = reverse('pets')
        pet = create_sample_pet()
        res = self.client.get(url)

        self.assertContains(res, pet.name)
        self.assertContains(res, pet.city)
        self.assertContains(res, pet.race)
        self.assertContains(res, pet.age)
        self.assertContains(res, pet.gender)
        self.assertContains(res, pet.size)

    def test_pet_has_page(self):
        """Test that pet has its own page"""
        pet = create_sample_pet()
        url = reverse('pet', args=[pet.id])
        print(url)
        res = self.client.get(url)

        self.assertContains(res, pet.name)
        self.assertContains(res, pet.city)
        self.assertContains(res, pet.race)
        self.assertContains(res, pet.age)
        self.assertContains(res, pet.gender)
        self.assertContains(res, pet.size)

    def test_search_form(self):
        """Test that search form works properly"""
        pet = create_sample_pet()
        url = reverse('pets')
        url = url + "?city={}&gender={}&age={}&size={}".format(pet.city,
                                                               pet.gender,
                                                               pet.age,
                                                               pet.size)
        print(url)
        res = self.client.get(url)

        self.assertContains(res, pet.name)
        self.assertContains(res, pet.city)
        self.assertContains(res, pet.race)
        self.assertContains(res, pet.age)
        self.assertContains(res, pet.gender)
        self.assertContains(res, pet.size)
