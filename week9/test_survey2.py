import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """"Tests for the class AnonymousSurvey"""
    def setUp(self):
        question = "What language did you first learn? "
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Java', 'C++', 'Python']
        
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()