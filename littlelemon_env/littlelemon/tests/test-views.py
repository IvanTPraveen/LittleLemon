from django.test import TestCase
from restaurant.views import *
from restaurant.models import *

class MenuViewTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(title = "icetea", price = 1.57, inventory = 101)
        self.item2 = Menu.objects.create(title = "ramen", price = 2.45, inventory = 234)
        self.item3 = Menu.objects.create(title = "chickenwings", price = 3.46, inventory = 220)
    def test_getall(self):
        self.assertEqual(str(self.item), "icetea : 1.57")
        self.assertEqual(str(self.item2), "ramen : 2.45")
        self.assertEqual(str(self.item3), "chickenwings : 3.46")