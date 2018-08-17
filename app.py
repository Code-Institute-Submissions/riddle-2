import os
from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
import json
import random
app = Flask(__name__)
with open("data/quiz.json","r") as info:
            data = json.load(info)
counter_dict = {}


@app.route('/',methods=['GET','POST'] )
def login():
    if request.method == "POST": 
        with open("data/reg-detail.txt","r") as fp:  
            valid_users = fp.read().splitlines()
            username = request.form['username']
            password = request.form['password']
            if username + ':' + password == valid_users:
                return "hi"
            else:
                return redirect('/register')
    return render_template('index.html')
        
    

    
# quiz 
@app.route('/quiz', methods=['GET','POST'])
def quiz():
   
    counter_dict = 0
    if request.method == "POST" :
         if data[counter_dict]["answer"] == (request.form["Answer"]):
              counter_dict += 1
            
    return render_template('quiz.html', data=data ,i=counter_dict)
    
#create an register form 
@app.route('/register', methods=['GET','POST'])
def register():
     if request.method =="POST":
            with open("data/reg-detail.txt","a") as register_Detail:
                register_Detail.writelines(request.form["username"]+ "\t")
                register_Detail.writelines(request.form["Password"]+ "\n")
                return redirect('/quiz')
     return render_template('register.html')
#create an login form 


app.run(host=os.getenv('IP'),
        port=int(os.getenv('PORT')),
        debug=True)
