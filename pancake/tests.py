from django.test import SimpleTestCase
from django.urls import reverse

from .views import IndexView


class HomeTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_view_by_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    

