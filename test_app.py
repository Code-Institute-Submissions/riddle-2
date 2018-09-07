import unittest
import app
app.testing = True
class TestQuiz(unittest.TestCase):
    def test_the_test(self):
        """
        Just to make sure that our testing is working
        """
        self.assertEqual(1,1)
   
    def test_sort_high_score(self):
        """
        Test that our sorted is properly sorting the score in descending order 
        """
        result = app.get_score()
        top_score = [('Priya',11),('Ram',10),('ajil',7)]
        self.assertEqual(result,top_score)
    
    
    def test_question_len(self):
        """
        Test to make sure that our 12 questions can be readable  
        """
        response = app.data
        self.assertEqual(len(response),12)
        
    
print("Test passed")
    
if __name__ == "__main__": 
      unittest.main() 