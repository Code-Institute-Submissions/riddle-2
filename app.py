import os
from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
from wtforms import form, StringField, TextAreaField, PasswordField, validators, Form
from passlib.hash import sha256_crypt

app = Flask(__name__)


    
@app.route('/')
def index():
    return render_template('index.html')
    
#create an login form 

@app.route('/register', methods=['GET','POST'])
#create an register form 
def register():
        if request.method =="POST":
            with open("data/register.txt","a") as register_Detail:
                register_Detail.writelines(request.form["username"] + "\t")
                register_Detail.writelines(request.form["email"] + "\t")
                register_Detail.writelines(request.form["Password"] + "\n")
                return redirect('/')
        return render_template('register.html')  
       
    
app.run(host=os.getenv('IP'),
        port=int(os.getenv('PORT')),
        debug=True)