from unittest import TestCase
from getPPCData import GetPPCData


class TestGetPPCData(TestCase):
    def test_get_toppings(self):
        self.assertEqual(len(GetPPCData.get_toppings()), 8)

    def test_get_prices(self):
        self.assertEqual(len(GetPPCData.get_prices()), 6)
