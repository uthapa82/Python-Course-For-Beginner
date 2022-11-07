import unittest
from names import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for names.py 
    """   
    def test_first_last_name(self):
        """testing with names like "Anup Thapa"
        """       
        formatted_name = get_formatted_name("Anup", "Thapa")
        self.assertEqual(formatted_name, "Anup Thapa")
        
    def test_first_last_middle_name(self):
        """Testing with "Ram Bdr Lamichhane"""
        formatted_name = get_formatted_name("Ram", "Lamichhane", "Bdr")
        self.assertEqual(formatted_name, "Ram Bdr Lamichhane")
        
unittest.main()