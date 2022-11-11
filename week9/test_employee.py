import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test case for employee."""
    def setUp(self):
        """test of employee."""
        self.abhi = Employee('abhi', 'lamichhane', 8000)

    def test_give_default_raise(self):
        """test the given default rise of employee."""
        self.abhi.give_rise()
        self.assertEqual(self.abhi.annual_salary, 13000)

    def test_give_custom_raise(self):
        """Test custom raise"""
        self.abhi.give_rise(10000)
        self.assertEqual(self.abhi.annual_salary, 18000)

unittest.main()