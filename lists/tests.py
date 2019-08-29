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

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do List', html)
        self.assertTrue(html.endswith('</html>'))
