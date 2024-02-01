import unittest
from restaurant.models import *

class MenuItemTest(unittest.TestCase):
    def test_model_case(self):
        item = Menu.objects.create(title="icecream", price=1, inventory=2)
        self.assertEqual('icecream : 1', item)