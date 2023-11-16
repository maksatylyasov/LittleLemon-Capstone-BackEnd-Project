from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer


# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")


# # TestCase class
# class TestMenu(TestCase):
#     def test_get_item(self):
#         item = Menu.objects.create(title="Pizza", price=80, inventory=100)
#         self.assertEqual(item.title, "Pizza")


# class TestSimple(TestCase):
#     def test_homepage(self):
#         response = self.client.get(reverse("home"))
#         self.assertEqual(response.status_code, 200)


# class MenuModelTest(TestCase):
#     def setUp(self):
#         # Set up non-modified objects used by all test methods
#         Menu.objects.create(title="Pizza", price=19.99, inventory=100)

#     def test_title_label(self):
#         menu = Menu.objects.get(id=1)
#         field_label = menu._meta.get_field("title").verbose_name
#         self.assertEqual(field_label, "title")

#     def test_price_label(self):
#         menu = Menu.objects.get(id=1)
#         field_label = menu._meta.get_field("price").verbose_name
#         self.assertEqual(field_label, "price")

#     def test_inventory_label(self):
#         menu = Menu.objects.get(id=1)
#         field_label = menu._meta.get_field("inventory").verbose_name
#         self.assertEqual(field_label, "inventory")

#     def test_string_representation(self):
#         menu = Menu.objects.get(id=1)
#         expected_object_name = f"{menu.title}"
#         self.assertEqual(str(menu), expected_object_name)


# class MenuViewTest(TestCase):
#     def setUp(self):
#         # Create test instances of Menu model
#         Menu.objects.create(title="Pizza", price=9.99)
#         Menu.objects.create(title="Burger", price=4.99)
#         # ... more instances as needed

#     def test_getall(self):
#         client = APIClient()
#         response = client.get(
#             reverse("menu-list")
#         )  # Adjust 'menu-list' to your URL name
#         menus = Menu.objects.all()
#         serializer = MenuSerializer(menus, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
