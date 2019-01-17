from django.test import TestCase, Client
from django.urls import reverse


class PagesTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        """Test that the index page works"""
        url = reverse('index')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_about_page(self):
        """Test that the about page works"""
        url = reverse('about')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
