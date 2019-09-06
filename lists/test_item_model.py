from lists.models import ToDoItem
from django.test import TestCase

class ToDoItemModelTest(TestCase):

    def test_save_and_retrieve_items(self):
        item1 = ToDoItem()
        item1.description = '1st item in DB'
        item1.save()

        items = ToDoItem.objects.all()

        self.assertEqual(items.count(), 1)
        self.assertEqual(items[0].description, '1st item in DB')
