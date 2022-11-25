import unittest

from country_code import get_country_code

class CountryCodeTestCase(unittest.TestCase):
    """testing country code class."""

    def test_get_country_code(self):
        country_code = get_country_code('United Arab Emirates')
        self.assertEqual(country_code, 'ae')

        country_code = get_country_code('Afghanistan')
        self.assertEqual(country_code, 'af')

unittest.main()