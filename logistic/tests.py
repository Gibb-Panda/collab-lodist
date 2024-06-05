import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from system.models import ConfigUser, CustomPermission, Role

from .models import Commodity, GoodHazardClass, StorageCondition, Warehouse


class CommodityTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Get or create the "Root" role and assign it to the test user
        root_role, created = Role.objects.get_or_create(name="Root")

        if created:
            # Create and assign necessary permissions to the root role if it was just created
            permissions = [
                "logistic.commodity.create",
                "logistic.commodity.read",
                "logistic.commodity.update",
                "logistic.commodity.delete",
            ]
            for perm in permissions:
                permission = CustomPermission.objects.create(
                    value=perm, description=f"Can {perm}"
                )
                root_role.permissions.add(permission)

        # Create a ConfigUser instance for the test user and assign the root role
        ConfigUser.objects.create(user=self.user, role=root_role)

        # Simulate login to obtain access and refresh tokens
        login_url = reverse("login")  # Adjust the URL to match your login endpoint
        login_data = {"username": "testuser", "password": "testpass"}
        response = self.client.post(login_url, login_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.data["access"]
        refresh_token = response.data["refresh"]

        # Set tokens in session for authentication
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        # Create related objects
        self.warehouse = Warehouse.objects.create(
            name_of_location="Main Warehouse",
            address="123 Warehouse St.",
            contact_information="contact@warehouse.com",
            storage_capacity=1000,
            horse_power=500,
            capacity=2000,
            load_capacity=1500,
            insurance_information="Insurance Details",
            responsible=self.user,
        )

        self.storage_condition = StorageCondition.objects.create(
            title="Cool Storage", condition="Cool", warehouse=self.warehouse
        )
        self.good_hazard_class = GoodHazardClass.objects.create(class_name="Class A")

        self.commodity_data = {
            "article_number": "12345",
            "product_name": "Test Product",
            "weight": 10,
            "length_dimension": 20,
            "height_dimension": 5,
            "country_of_origin": "Country X",
            "expiry_date": datetime.date.today(),
            "customs_tariff_number": "54321",
            "packaging_information": "Box",
            "insurance_value": 1000,
            "position": "Aisle 3",
            "storage_condition": self.storage_condition.id,
            "good_hazard_class": self.good_hazard_class.id,
            "warehouse": self.warehouse.id,
        }

    def test_create_commodity(self):
        url = reverse("commodity_api")
        response = self.client.post(url, self.commodity_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Commodity.objects.count(), 1)
        self.assertEqual(Commodity.objects.get().article_number, "12345")

    def test_retrieve_commodity(self):
        commodity_data = self.commodity_data.copy()
        commodity_data["storage_condition"] = self.storage_condition
        commodity_data["good_hazard_class"] = self.good_hazard_class
        commodity_data["warehouse"] = self.warehouse
        commodity = Commodity.objects.create(**commodity_data)
        url = reverse("commodity_api_detail", args=[commodity.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["article_number"], commodity.article_number)

    def test_update_commodity(self):
        commodity_data = self.commodity_data.copy()
        commodity_data["storage_condition"] = self.storage_condition
        commodity_data["good_hazard_class"] = self.good_hazard_class
        commodity_data["warehouse"] = self.warehouse
        commodity = Commodity.objects.create(**commodity_data)
        url = reverse("commodity_api_detail", args=[commodity.id])

        update_data = self.commodity_data.copy()
        update_data["product_name"] = "Updated Product"
        response = self.client.put(url, update_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        commodity.refresh_from_db()
        self.assertEqual(commodity.product_name, "Updated Product")

    def test_partial_update_commodity(self):
        commodity_data = self.commodity_data.copy()
        commodity_data["storage_condition"] = self.storage_condition
        commodity_data["good_hazard_class"] = self.good_hazard_class
        commodity_data["warehouse"] = self.warehouse
        commodity = Commodity.objects.create(**commodity_data)
        url = reverse("commodity_api_detail", args=[commodity.id])
        update_data = {"product_name": "Partially Updated Product"}
        response = self.client.patch(url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        commodity.refresh_from_db()
        self.assertEqual(commodity.product_name, "Partially Updated Product")

    def test_delete_commodity(self):
        commodity_data = self.commodity_data.copy()
        commodity_data["storage_condition"] = self.storage_condition
        commodity_data["good_hazard_class"] = self.good_hazard_class
        commodity_data["warehouse"] = self.warehouse
        commodity = Commodity.objects.create(**commodity_data)
        url = reverse("commodity_api_detail", args=[commodity.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Commodity.objects.count(), 0)
