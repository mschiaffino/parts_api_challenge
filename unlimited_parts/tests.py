from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from unlimited_parts.models import Part

# region Models tests


class PartTestCase(TestCase):
    def setUp(self):
        Part.objects.create(
            name="Heavy Coil",
            sku="SDJDDH8223DHJ",
            description="Tightly wound nickel-gravy alloy spring",
            weight_ounces=22,
            is_active=1,
        )

    def test_create_part(self):
        """Parts can be successfully created"""
        heavy_coil_part = Part.objects.get(pk=1)

        self.assertEqual(heavy_coil_part.name, "Heavy Coil")
        self.assertEqual(heavy_coil_part.sku, "SDJDDH8223DHJ")
        self.assertEqual(
            heavy_coil_part.description, "Tightly wound nickel-gravy alloy spring"
        )
        self.assertEqual(heavy_coil_part.weight_ounces, 22)
        self.assertEqual(heavy_coil_part.is_active, 1)
        self.assertEqual(Part.objects.count(), 1)

    def test_delete_part(self):
        """Parts can be successfully deleted"""
        Part.objects.get(pk=1).delete()

        self.assertEqual(Part.objects.count(), 0)


# endregion

# region Views tests


class PartViewsetTest(APITestCase):
    def setUp(self):
        Part.objects.create(
            name="Heavy Coil",
            sku="SDJDDH8223DHJ",
            description="Tightly wound nickel-gravy alloy spring",
            weight_ounces=22,
            is_active=1,
        )

    def test_list_all_parts(self):
        response = self.client.get("/parts/")

        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "Heavy Coil",
                    "sku": "SDJDDH8223DHJ",
                    "description": "Tightly wound nickel-gravy alloy spring",
                    "weightOunces": 22,
                    "isActive": 1,
                }
            ],
        )

    def test_create_part(self):
        data = {
            "name": "Reverse Lever",
            "sku": "DCMM39823DSJD",
            "description": "Attached to provide inverse leverage",
            "weightOunces": 9,
            "isActive": 0,
        }
        response = self.client.post("/parts/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Part.objects.count(), 2)
        self.assertEqual(Part.objects.get(pk=2).name, "Reverse Lever")

    def test_patch_part(self):
        data = {"isActive": 0}
        response = self.client.patch("/parts/1/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Part.objects.get(pk=1).is_active, 0)

    def test_delete_part(self):
        response = self.client.delete("/parts/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Part.objects.count(), 0)


# endregion
