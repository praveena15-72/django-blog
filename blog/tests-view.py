from django.test import TestCase
from django.urls import reverse

class ViewTest(TestCase):

    def test_view_url_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_admin(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)
