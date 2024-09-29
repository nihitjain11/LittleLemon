from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        menu = Menu(title='Pizza', price=10, inventory=10)
        self.assertEqual(menu.get_item(), 'Pizza : 10')