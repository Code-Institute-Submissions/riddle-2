###### Ramanathan Annes
# Riddle-me-These 
These a quiz game with random question and it easy to access. These will help you to learn some new things around world.

### Features 
  Firstly, it have a login form to take the user straight to quiz these  only work when the user already  register 
  there username otherwise they can't acess the game.
  
  A quiz.html page that refreshes itself after each question, so the user can progress to the next and keeps track of the scoring.
  
  Even the answer is wrong the user will get to next question without adding the score.
  
### Technologies Used
  In this section, I  mention all of the languages, frameworks, libraries, and any other tools that I used to construct this project.
  - Bootstrap : 
       * I used a **Bootstrap** for design and UX
  - Font Awesome :
      * I used **Font Awesome** for better design and styling
  - Flask : 
     * The whole project mainly depend on **Flask**.
  - Wireframe : 
     * I used **Wireframe** to design the project. [Wireframe](https://www.lucidchart.com/invitations/accept/2e536758-5bda-4471-9015-599ee0e4f49b)

### Testing
   Manual testing to confirm that the correct question was being passed to the page.
   I did auto testing for check sorted is working.[Testing File](https://github.com/Ramanathan03/riddle/blob/master/test_app.py)
 
   
Another way I tested the quiz app by acting like a player and moving around the quiz to make user functionality is working.

| Functional      | Expected Output Y/N          | Pass Y/N| Explaination of the Functionality 
| ------------- |:-------------:| -----:|---:|
| **User login/register form**  |Yes|Yes|If user register their details before they can go to game straightly by using login form.otherwise,if user new to the game they have to register|
|**Counter/score Increment**|Yes|Yes|score will added only when question is right  |
|**Answer is Correct**|Yes|Yes|If answer is right user will access the next question and score will added|
|**Answer is Incorrect**|Yes|Yes|If answer is incorrect in 1st attempt user will get another chance if both answer is incorrect the score will be same but user will get to next question|
|**After Answered every question**|Yes|Yes|If user answered every question in the game they will redirect to gameover page |

##### Different screen sizes:
   I used  **Chrome development tool** to testing my quiz game responsible  in smaller screen and in large screen.
   
   - The quiz is quite responsive and works best on both large middle and small screen.
   - The look and feel remains the same in different sizes

###### website background image is not responsive  

### Deployment
This project was deployed on Heroku 
###### Here is the way to I depolyed to heroku 
 - git remote add heroku 
 - create procfile 
 - ps:scale web=1
 - Push to Heroku --> $ git push heroku master
 

##### Config Vars --> IP = 0.0.0.0, PORT = 5000

### Acknowledgements
Code Institute Mentor **Chris Zielinski** 
