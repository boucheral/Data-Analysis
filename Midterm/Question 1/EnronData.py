from email.parser import Parser
from email.message import EmailMessage
import glob
import os
import re

def parseEmailFile(fileName) :
    with open(fileName, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)
    return email

	
def getEmails(fileString) :
    l = []
    
    searchDirectory(fileString, l)
    
    return l

def searchDirectory(fileString, l) :
    names = glob.glob(fileString + '/*')
    
    for name in names :
        if (os.path.isdir(name)) :
            searchDirectory(name, l)
        elif (os.path.isfile(name)) :
            l.append(parseEmailFile(name))
  
 
