
from flask import Flask,render_template, request
from scrapper import WebScrapeNewUniversity
from scrapper import weather
from Main import CheckAccount, CreateAccount
from datetime import date, datetime,time
# from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
# import pandas as pd

zotHome = Flask(__name__)

@zotHome.route('/')
def home():
    newslist = WebScrapeNewUniversity()
    wet = weather()
    return render_template("home.html",newslist = newslist,weather = wet)

@zotHome.route("/SignIn",methods = ["GET","POST"])
def SignIn():
    if request.method == "POST":
        first_name = request.form.get("email_address")
        password = request.form.get("password")
        import logging
        logging.basicConfig(filename="useractivity.log",level=logging.INFO)
        #print ("Here")
        #print(CheckAccount(first_name,password))
        if CheckAccount(first_name,password) == True:
            logging.info(f"{first_name} user logged in at {datetime.now()} ")
            #print("It comes here")
            return render_template("links.html",first_name = first_name)
        else:
            logging.error(f"{first_name} user logged in at {datetime.now()} but resulted in invalid password or username")
            return "Invalid Username or Password"
    return render_template("SignIn.html")

@zotHome.route("/links")
def Links():
    return render_template("links.html")

@zotHome.route("/SignUp",methods = ["GET","POST"])
def SignUp():
    if request.method == "POST":
        first_name = request.form.get("email_address")
        password = request.form.get("password")
        reply=CreateAccount(first_name,password)
        if reply == True:
            #TODO: Insert POPUP for Account Created!
            return render_template("SignIn.html")
        else:
            return "Username Already exists!"
    return render_template("SignUp.html")

@zotHome.route("/aboutus")
def AboutUs():
    return render_template("aboutus.html")


@zotHome.route("/TaC")
def TaC():
    return render_template("TaC.html")
# @zotHome.route("/successfulsignin",methods=["POST"])
# def successfulsignin():
#     return render_template("successfulsignin.html",first_name = first_name, password = password)


if __name__ =="__main__":
    zotHome.run()
