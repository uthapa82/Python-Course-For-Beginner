class Employee():
    """class of employee."""

    def __init__(self, first_name, last_name, annulal_salary):
        """Initialize the employee info."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annulal_salary

    def give_rise(self, amount=5000):
        """give rise to employees."""
        self.annual_salary += amount 