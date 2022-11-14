#! /usr/bin/python3

print("Content-type: text/html\n\n")

import sys
import hashlib 
import mysql.connector
import struct
import cgi

mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "fgs20228",
        port = "3305",
        database = "users"
        )
mycursor = mydb.cursor(buffered=True,dictionary=True)

form = cgi.FieldStorage()

email = form["emailInput"].value
password = hashlib.sha512(form["password"].value.encode()).hexdigest()

mycursor.execute(f"SELECT password FROM users WHERE email=\"{email}\";")

try:
    (passwordCorB,) = mycursor.fetchall()
    passwordCor = passwordCorB["password"]
    if(passwordCor != password):
        print("invalid pass")
    else:
        mycursor.execute(f"SELECT firstName FROM users WHERE email=\"{email}\";")
        (nameBuf,) = mycursor.fetchall()
        print("hello "+ nameBuf["firstName"])
except:
    print("Invalid Input")
