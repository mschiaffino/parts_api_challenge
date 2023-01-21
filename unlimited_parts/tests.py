from django.test import TestCase

from unlimited_parts.models import Part


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
