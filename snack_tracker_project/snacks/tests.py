from urllib import request
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack
from django.contrib.auth.models import User


class SnackTest(TestCase):
    def setUp(self):
        self.detail_url = reverse("snack_detail", args=['1'])
        kebab_snack = Snack.objects.create(
            name='Kebab',
            description='BBQ meal',
            purchaser=User.objects.create_user(
                'john', 'lennon@thebeatles.com', 'johnpassword')
        )

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_detail_page_status_code(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        detail_url = reverse("snack_detail", args=['1'])
        response = self.client.get(detail_url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "_base.html")
