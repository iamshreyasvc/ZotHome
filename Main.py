# ZotHome Projext by Shreyas Vasist Chandramouli
import os
import sys
import Inputs

class User():
    '''Defines a user and allows its properties to be stored'''
    def __init__(self):
        self.username =""
        self.password =""
        self.bio=""

    def SetUsername(self):
        Username = Inputs.TakeUsername
        self.username = Username
    
    def SetPassword(self):
        Password = Inputs.TakePassword
        self.password = Password


