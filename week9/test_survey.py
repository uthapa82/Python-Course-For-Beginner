import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """"Tests for the class AnonymousSurvey"""
      
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question =  "What language did you first learn ? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("C++")
        
        self.assertIn('C++', my_survey.responses)
    
    def test_store_three_responses(self):
        question = "What language did you first learn ?"
        my_survey = AnonymousSurvey(question)
        responses = ["Java", "c"]
        for response in responses:
            my_survey.store_response(response)
            
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()