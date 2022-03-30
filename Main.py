# ZotHome Project by Shreyas Vasist Chandramouli
import pathlib
from email.headerregistry import Address
from logging import exception
import random
import os
import sys
import requests

#extremely inefficent for large number of values!
#MUST BE STREAMLINED!
def CreateAccount(email_address,password):
    Listofitems = []
    DictofItems ={}
    openfile = open("Personal_Projects\ZotHome\profiles.txt","r")
    values = openfile.readlines()
    openfile.close()
    for value in values:
        Listofitems.append(value.strip("\n"))
    for item in Listofitems:
        DictofItems[item.split()[0]] = item.split()[1]
    if email_address not in DictofItems.keys():
        openfile = open("Personal_Projects\ZotHome\profiles.txt","a")
        openfile.writelines(f"{email_address} {password}\n")
        return True
    else:
        return False
        
#extremely inefficent for large number of values!
# MUST BE STREAMLINED!
def CheckAccount(email_address = None, password=None):
    Listofitems = []
    DictofItems ={}
    print(pathlib.Path().absolute())
    openfile = open("Personal_Projects\ZotHome\profiles.txt","r")
    values = openfile.readlines()
    openfile.close()
    for value in values:
        Listofitems.append(value.strip("\n"))
    for item in Listofitems:
        DictofItems[item.split()[0]] = item.split()[1]
    if email_address in DictofItems.keys():
        if DictofItems[email_address] == password:
            return True
        else:
            return False
    else:
        return False

#print(CheckAccount("svchand1@uci.edu","shreyas123"))

class Human():

    def __init__(self,name,age,DOB,gender,addr, SexualO = None,HumanType = "unclassified") -> None:
        if name is not None and age is not None and DOB is not None and gender is not None:
            self.name = name
            self.age = age
            self.DOB = DOB
            self.gender = gender
            self.sexualO = SexualO
            self.addr = addr
            self.type = HumanType
            self.UniqueID = 000000

        else: raise TypeError(f"Essential Values [Name: {name},Age: {age},DOB: {DOB},Gender: {gender}] have not been entered properly! ")


    
    def GenerateUID(self):
        openfile = open("people.txt","r")
        lines = openfile.readlines()
        #print(lines)
        for line in lines:
            line = line.strip().split()
        UniqueID = random.randint(10000000,99999999)
        for value in lines:
            if str(UniqueID) in value:
                pass

        self.UniqueID = UniqueID



    def storevalue(self):
        openfile = open("people.txt","a")
        openfile.writelines(f"{self.UniqueID} {self.name} {self.DOB} {self.gender} {self.sexualO} {self.addr} {self.type} \n")




# shreyas = Human("Shreyas",19,"02/21/2003","M","4073 Mesa",)
# shreyas.storevalue()
# shreyas.GenerateUID()
# shreyas.storevalue()

# UserName = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# DateofBirth = str(input("Enter your Date of Birth: "))
# Gender = str(input("Enter your Gender: "))
# addr = str(input("Enter your Address: "))



# Nandini = Human(UserName,age,DateofBirth,Gender,addr)
# Nandini.GenerateUID()
# Nandini.storevalue()






