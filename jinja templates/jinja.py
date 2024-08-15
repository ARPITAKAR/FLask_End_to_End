from flask import Flask,render_template,url_for
from employees import employees_data
# rendering the pages of html-->render_templates
# create object app module
# Flask ko bol rahe hai ki iss module __name__=="__main__" mei application  hai
# Flask has an inbuilt function parameter as template_folder="templates" so this is the convention
app=Flask(__name__ )
# /forward slash means homepage
@app.route("/")
# creating the endpoint
@app.route("/home")
## For same function we can have different Routes
def home():
    return render_template("home.html",title='Homepage')
@app.route("/about")
def about():
    # title is the parameter 
    return render_template("about.html",title='Aboutpage')

## what is jinja it's simply a tool to load dynamic web pages....
# matlab whatever we change at backend it will get updated soon after implementation
# jinja has four major use cases parameters and placeholder if condtionoals for loopes blocks
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html", title="Evaluate", number=num)

@app.route("/employees")
def employees():
    return render_template("employees.html",title="Employees",emps=employees_data)

@app.route("/employees/managers")
def managers():
    return render_template("managers.html",title="Managers",emps=employees_data)

#Format for placeholder in ninja {{TiTLE}}
if __name__=="__main__":
    app.run(debug=True)