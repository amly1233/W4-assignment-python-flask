from flask import Flask 
from flask import request
from flask import redirect
from flask import render_template
from flask import session, url_for

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# /
@app.route("/", methods=["GET"])
def index():
    if "username" in session and "password" in session:
        return render_template("member.html")
    return render_template("index.html")


# /login
@app.route("/signin", methods=["POST","GET"])
def signin():
    username=request.form["username"]
    username=str(username)
    password=request.form["password"]
    password=str(password)
    if username==password=="test":
        session["username"]=request.form["username"]
        session["password"]=request.form["password"]
        return redirect("/member")
    else:
        return render_template("error.html")


# /member
@app.route("/member",methods=["POST","GET"])
def member():
    username=session.get("username")
    password=session.get("password")
    if  username==password=="test":
        return render_template("member.html")

    else:
        return render_template("index.html")

    
# /logout
@app.route("/signout",methods=["POST","GET"])
def signout():
    session.pop("username", None)
    session.pop("password", None)
    return redirect("/")


app.run(port=3000)