from django.test import TestCase

# Create your tests here.
# To run the test execute the following from 'django-todo-app' folder:
# python manage.py test
class HomePageTest(TestCase):
    def test_smoke_test(self):
        self.assertEqual(1+1, 3)
