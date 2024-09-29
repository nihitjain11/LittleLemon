from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuItemViewTest(APITestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(username='testuser', password='testpassword')
		self.client.force_authenticate(user=self.user)
		self.menu_item = Menu.objects.create(id=1,title='Pizza', price=10, inventory=10)
		self.url = reverse('menu')

	def test_get_menu_items(self):
		response = self.client.get(self.url)
		menu_items = Menu.objects.all()
		serializer = MenuSerializer(menu_items, many=True)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, serializer.data)

	def test_create_menu_item(self):
		data = {'id':99,'title': 'Burger', 'price': 15, 'inventory': 5}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Menu.objects.count(), 2)
		self.assertEqual(Menu.objects.get(id=response.data['id']).title, 'Burger')