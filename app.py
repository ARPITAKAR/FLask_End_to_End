from flask import Flask
# create object app module
# Flask ko bol rahe hai ki iss module __name__=="__main__" mei application  hai
app=Flask(__name__)
# /forward slash means homepage
@app.route("/")
# creating the endpoint
@app.route("/home")
## For same function we can have different Routes
def home():
    return "<h1> Welcome to my Home of Future </h1>"

@app.route("/about")
def about():
    return "<h3> I will become Data Scintist Earn money serve my parents and have family </h3>"

# <> we tell flask that we are expecting a parameter from the user end.
# {name.title} will capitalise first word of string provided
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hello {name} Live High Live long Never put yourself down </h1>"
# give integar input as <int:num>
@app.route("/addition/<int:num>")
def addition(num):
    return f"input is {num}, output is {num+10}"
# slash lga te jao input badha te jaao,  function name bust be different each time here in FLASK
@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1,num2):
    return f"input is {num1} and {num2}, output is {num1+num2}"


if __name__=="__main__":
    app.run(debug=True)