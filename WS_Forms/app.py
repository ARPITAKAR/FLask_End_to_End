from flask import Flask,render_template,redirect,url_for,flash
# From form.py we are calling two classes
from form import SignupForm, LoginForm
app=Flask(__name__)
app.config["SECRET_KEY"]="This_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")


@app.route("/signup", methods=["GET","POST"])
def signup():
    form=SignupForm()
    # if there is any field requirements not satisfied give back the Error
    # When we click submit button and all the fields are correct go to the home page else remain on signup page
    if form.validate_on_submit():
        flash(f"Succesfully registered {form.username.data}!")
        return redirect(url_for("home"))
    return render_template("signup.html",title="SIGNUP",form=form)


@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    # Validating what user given input to
    email= form.email.data
    pw=form.password.data
    if form.validate_on_submit():
        if email=="arpit1004@gmail.com" and pw=='12345':
            flash("Logged in Succesfully!")
            return redirect(url_for("home"))
        else:
            flash("incorrect email and password")
    return render_template("login.html",title="Logging",form=form)

if __name__=="__main__":
    app.run(debug=True)
