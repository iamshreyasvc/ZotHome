def TakeUsername():
    try:
        UserInput = str(input("Enter your desired Username: "))
        return UserInput
    except TypeError:
        print("Error! Please input valid password")
        TakeUsername()

def TakePassword():
    try:
        UserInput = str(input("Enter your desired Password: "))
        return UserInput
    except TypeError:
        print("Error! Please input valid password")
        TakePassword()

import cgi
import cgitb #found this but isn't used?

form = cgi.FieldStorage()

user_name = form.getvalue('username').capitalize()
password = form.getvalue('password').capitalize()

print(user_name)
print(password)
