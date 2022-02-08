from flask import Flask,render_template

zotHome = Flask(__name__)

@zotHome.route('/')
def home():
    return render_template("home.html")

@zotHome.route("/SignIn")
def SignIn():
    return render_template("SignIn.html")

@zotHome.route("/links")
def Links():
    return render_template("links.html")

@zotHome.route("/aboutus")
def AboutUs():
    return render_template("aboutus.html")

if __name__ =="__main__":
    zotHome.run()
