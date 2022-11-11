import unittest

from city_function import city_country

class CitiesTestCase(unittest.TestCase):
    """Test exercise 'city_function.py'."""

    def test_city_country(self):
        """Does name of city and country pair work."""
        formatted_name = city_country('Santiago', 'Chile')
        self.assertEqual(formatted_name, 'Santiago Chile')

unittest.main()