import os
from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
import json
import random

app = Flask(__name__)
app.secret_key = 'some_secret'

with open("data/quiz.json","r") as info:
    data = json.load(info)

    
# counter_dict = {}


#create an login form 
@app.route('/',methods=['GET','POST'] )
def login():
    if request.method == "POST":
        with open("data/reg-detail.txt","r") as fp:  
            valid_users = fp.read().splitlines()
            print(valid_users)
            username = request.form['username']
            password = request.form['password']
            if username + ':' + password in valid_users:
                return redirect('/quiz')
            else:
                return redirect('/register')
                
    return render_template('index.html',page_title="Go over |Home")
        


    
# quiz 
@app.route('/quiz', methods=['GET','POST'])
def quiz():
    
    counter = 0# If it's a GET request we start the counter at 0
    score = 0
    if request.method == "POST":
        counter = int(request.form["current_question_number"])
        score = int(request.form["current_score"])
        # Overwrite the counter if this is a post request
        print(data[counter]["answer"], request.form["Answer"])
        if counter == 11:
            return redirect('/gameover')
        else:
         if data[counter]["answer"] == (request.form["Answer"]):
            # Increment score
            # increment the counter
            # Possibly return a new variable for play_sound=True
            # Handle what to do on the last question
            flash('Right Keep push yourself!')
            counter += 1
            score += 1
            print(score)
         
         else:
            flash('last question answer is wrong ')
            counter += 1
            print(score)
            
    return render_template('quiz.html', data=data,i=counter, s=score,page_title="Quiz")

@app.route('/gameover')
def gameover():
    return render_template('GG.html',page_title="GAME OVER |quiz")
#create an register form 
@app.route('/register', methods=['GET','POST'])
def register():
     if request.method =="POST":
                 with open("data/reg-detail.txt","a") as register_Detail:
                     register_Detail.writelines(request.form["username"]+ ":")
                     register_Detail.writelines(request.form["Password"]+ "\n")
                     return redirect('/quiz')
     return render_template('register.html',page_title="Register")



app.run(host=os.getenv('IP'),
        port=int(os.getenv('PORT')),
        debug=True)
