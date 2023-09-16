from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username="nacer",
            email="nacer@ept.sn",
            first_name="nacer",
            last_name="Eddine"
        )

    def test_user_model(self):
        user = User.objects.get(username="nacer")
        self.assertEqual(user.username, "nacer")
        self.assertEqual(user.email, "nacer@ept.sn")
        self.assertEqual(user.first_name, "nacer")
        self.assertEqual(user.last_name, "Eddine")


    def test_list_users(self):
        url = reverse("get all users")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), User.objects.count())


class CountVisitsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_count_visits_first_visit(self):
        url = reverse("count number of visits")  
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('visit_count'), 1)

    def test_count_visits_subsequent_visits(self):

        url = reverse("count number of visits") 
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('visit_count'), 1)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('visit_count'), 2)
