from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from lists.models import ToDoItem

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

    def test_can_save_a_post_request(self):
        post_response = self.client.post('/', {'item_text': 'my first to-do item'})
        self.assertEqual(ToDoItem.objects.count(), 1)
        self.assertIn('my first to-do item', post_response.content.decode())

    def test_do_not_save_items_on_a_get_request(self):
        self.client.get('/')
        self.assertEqual(ToDoItem.objects.count(), 0)
