
import unittest
import app
app.testing = True
class TestQuiz(unittest.TestCase):
    def test_question(self):
           self.assertEqual(1,1)
    # tests:
    # Before any of this, make sure you know how to make GET/POST requests
    # Scores are being calculated properly
    # Login returns a redirect
    # Username exists in the session after logging in
    # Test that riddle counter works properly
    # Test that answer checking functionality works
    # Test that username and password are correctly added to the register file
    
        
       
    def test_registration_works(self):
          post_method = app.request.POST('/register') and app.register()
          with open("data/reg-detail.txt","r") as register_Detail:
                self.assertIn(post_method, register_Detail) 
        #1. Make a POST to /register
    #     2. Open the register_detail
    #     3. Verify that register_detail has the username and password you POSTed in step 1
        
    
    # def test_counter(self):
    #     session = {}
    #     session['username'] = 'test_user'
    #     session['score'] = 0
    #     session['counter'] = 0
    #     data = {}
    #     data['session'] = session
    #     url = '/quiz'
    #     response = request.post(url, data=data)
    #     print(response)
    #def test_load_questions(self):
    
    # def test_login_returns_redirect(self):
    #     pass
    #     # test that login returns a redirect (status 302)
        
      
print("Test passed")
    

if __name__ == "__main__": 
      unittest.main() 