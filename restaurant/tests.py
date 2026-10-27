from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Booking, MenuItem

User = get_user_model()

class MenuAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = MenuItem.objects.create(title="Greek Salad", price="12.50", inventory=10)

    def test_menu_list_is_public(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Greek Salad")

    def test_menu_create_requires_staff(self):
        response = self.client.post("/api/menu/", {
            "title": "Pasta", "price": "15.00", "inventory": 5
        }, format="json")
        self.assertEqual(response.status_code, 403)

class BookingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="tester", password="StrongPass123!")
        self.client.force_authenticate(user=self.user)

    def test_authenticated_user_can_create_booking(self):
        response = self.client.post("/api/bookings/", {
            "name": "Test Guest",
            "no_of_guests": 2,
            "booking_date": (timezone.now() + timedelta(days=1)).isoformat(),
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().user, self.user)

class RegistrationAPITests(TestCase):
    def test_registration_creates_user_and_token(self):
        response = self.client.post("/api/registration/", {
            "username": "newuser", "email": "new@example.com",
            "password": "StrongPass123!"
        }, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn("token", response.json())
