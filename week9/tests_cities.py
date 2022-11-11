import unittest

from citys_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """testing 'citi_function.py'"""

    def test_city_country(self):
        """Does string city and country pair work?""" 
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual = (santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """Testing with population argument"""
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago Chile -population 5000000')

unittest.main()