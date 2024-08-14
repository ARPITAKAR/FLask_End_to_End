from flask import Flask,redirect,url_for
import time
app=Flask(__name__)

@app.route("/")

def home():
    return "<h1> Welcome to the home page</h1>"

@app.route("/pass")
def passed():
    return "<h1> Welcome Brother you had achieved</h1>"

@app.route("/Fail")
def failed():
    return "<h1> Work Hard, Work work work work> </h1>"

@app.route("/score/<name>/<int:num>")

def score(name,num):
    if num<30:
        time.sleep(1)
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        return redirect(url_for("passed"))
if __name__=="__main__":
    app.run(debug=True)