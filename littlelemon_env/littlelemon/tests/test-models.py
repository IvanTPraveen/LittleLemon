from django.test import TestCase
from restaurant.models import *

class MenuItemTest(TestCase):
    def test_model_case(self):
        item = Menu.objects.create(title="icecream", price=1.56, inventory=100)
        self.assertEqual(str(item), 'icecream : 1.56')