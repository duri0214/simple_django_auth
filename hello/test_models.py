from django.test import TestCase

from hello.models import Facility


class TestFacility(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        Facility.objects.create(code="001", name="Test Market")

    def test_market_content(self):
        market = Facility.objects.get(id=1)
        expected_object_name = f"{market.code}"
        self.assertEquals(expected_object_name, "001")
        expected_object_name = f"{market.name}"
        self.assertEquals(expected_object_name, "Test Market")

    def test_market_count(self):
        # Check that there is only one market object in the database
        market_count = Facility.objects.all().count()
        self.assertEqual(market_count, 1)
