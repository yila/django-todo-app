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

    def test_use_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_handles_post_request(self):
        post_response = self.client.post('/', {'item_text': 'my first to-do item'})
        self.assertIn('my first to-do item', post_response.content.decode())
