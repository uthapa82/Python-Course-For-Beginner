import unittest
from city_function import city_country

class CitiesTestCase(unittest.TestCase):
    """Test exercise 'city_function.py'."""

    def test_city_country(self):
        """Does name of city and country pair work."""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'santiago chile')

unittest.main()