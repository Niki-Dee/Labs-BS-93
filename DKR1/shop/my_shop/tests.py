from django.test import TestCase
from .models import Item
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class ShopTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        num = 13
        for number in range(num):
            Item.objects.create(name='name %s' % number, detail='details %s' % number, price = 10 )

    def test_view_url_accessible_by_name(self):
        resp = self.client.get('register/create')
        self.assertEqual(resp.status_code, 404)

    def test_name_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        author=Item.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length,100)

    def test_detail_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('detail').verbose_name
        self.assertEquals(field_label, 'detail')

    def test_name_max_length_(self):
        author=Item.objects.get(id=1)
        max_length = author._meta.get_field('detail').max_length
        self.assertEquals(max_length,2000)