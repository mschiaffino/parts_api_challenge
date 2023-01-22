from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from unlimited_parts.models import Part
from unlimited_parts.models import DescriptionWordCount

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

    # region DescriptionWord updates tests

    def test_creates_description_word_count_records(self):
        """Creating a part updates desciption word count recods"""
        Part.objects.create(
            name="Alloy Steel Bar",
            sku="SFSDF8SDGF",
            description="Tight-tolerance hardened multipurpose alloy steel bar",
            weight_ounces=22,
            is_active=1,
        )

        self.assertEqual(DescriptionWordCount.objects.get(pk="tight").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="tolerance").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="hardened").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="multipurpose").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="alloy").count, 2)
        self.assertEqual(DescriptionWordCount.objects.get(pk="steel").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="bar").count, 1)

    def test_substract_description_word_count(self):
        """Parts can be successfully deleted"""
        Part.objects.get(pk=1).delete()

        self.assertEqual(Part.objects.count(), 0)

        self.assertEqual(DescriptionWordCount.objects.get(pk="tightly").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="wound").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="nickel").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="gravy").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="alloy").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="spring").count, 0)

    def test_updates_description_word_count_records(self):
        """Updating a part updates desciption word count recods"""
        heavy_coil_part = Part.objects.get(pk=1)
        heavy_coil_part.description = "Super tightly wound spring"
        heavy_coil_part.save()

        self.assertEqual(DescriptionWordCount.objects.get(pk="super").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="tightly").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="wound").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="spring").count, 1)
        self.assertEqual(DescriptionWordCount.objects.get(pk="nickel").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="gravy").count, 0)
        self.assertEqual(DescriptionWordCount.objects.get(pk="alloy").count, 0)

    def test_does_not_save_empty_word(self):
        """Make sure that we do not save empty strings"""
        empty_word_query = DescriptionWordCount.objects.filter(pk="")
        self.assertFalse(empty_word_query.exists())

    # endregion


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


class DescriptionWordCountTest(APITestCase):
    def setUp(self):
        Part.objects.create(
            name="Heavy Coil",
            sku="SDJDDH8223DHJ",
            description="Tightly wound nickel-gravy alloy spring",
            weight_ounces=22,
            is_active=1,
        )

        Part.objects.create(
            name="Ultra Heavy Coil",
            sku="DCMM39823DSJD",
            description="Super tightly wound steel alloy spring",
            weight_ounces=9,
            is_active=0,
        )

    def test_returns_top_five_words(self):
        response = self.client.get("/top_part_description_words/")

        self.assertEqual(
            response.json(),
            [
                {"word": "alloy", "count": 2},
                {"word": "spring", "count": 2},
                {"word": "tightly", "count": 2},
                {"word": "wound", "count": 2},
                {"word": "gravy", "count": 1},
            ],
        )


# endregion
