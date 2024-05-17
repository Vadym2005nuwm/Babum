from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        def test_home_url_resolves_home_view(self):
            view = resolve('/')
            self.assertEquals(view.func.view_class,
                              HomePageView)



