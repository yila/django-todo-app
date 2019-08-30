from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
# To run the test execute the following from 'django-todo-app' folder:
# python manage.py test
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        resolveResult = resolve('/')
        self.assertEqual(resolveResult.func, home_page)

    def test_rendering_correct_file(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
