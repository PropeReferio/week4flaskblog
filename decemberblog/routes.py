#These are routes from our MVC (Model View Controller) model. Routes are part of our Controller
from decemberblog import app, db
from flask import render_template, request, redirect, url_for
from decemberblog.forms import SignupForm, LoginForm, PostForm

#From Werkzeug for Security Import
from werkzeug.security import check_password_hash

#Import for Flask-Login
from flask_login import login_user, current_user, login_required

#User Model Import
from decemberblog.models import User, Post

#Home Route
@app.route("/")
def home():
    #Display posts for logged in User
    posts = Post.query.all()
    return render_template("home.html", post = posts)

#Signup Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    signupForm = SignupForm() #Two variables and a class with same letters but different casing
    #This can be confusing, but this is convention.
    if request.method == "POST":
        username = signupForm.username.data
        email = signupForm.email.data
        password = signupForm.password.data
        print(username, email, password)
        #Add Form Data to User Model Class(AKA Database)
        #First import User Model(Above)
        #Second - Open a database session, then add our data
        user = User(username,email,password)
        db.session.add(user) #Start communication with database
        #Third - Commit and close the session for the database
        db.session.commit()

    return render_template("signup.html",signupform = signupForm)

#Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        #Find out who the logged in user currently is:
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))

    else:
        print("Not Valid Method")
    return render_template("login.html", loginform=loginForm)

@app.route('/post', methods = ["GET", "POST"])
@login_required
def post():
    postForm = PostForm()
    title = postForm.title.data
    content = postForm.content.data
    user_id = current_user.id
    print(title,content,user_id)

    
    #Saving Post Data to Database
    post = Post(title = title, content = content, user_id = user_id)
    db.session.add(post)
    db.session.commit()
    return render_template('create_post.html',postform=postForm)