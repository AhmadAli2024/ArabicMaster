#! /usr/bin/python3

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
        print("Location: http://localhost:1000/ArabicMaster/UserRegistration/login.html\n\n")
    else:
        mycursor.execute(f"SELECT firstName FROM users WHERE email=\"{email}\";")
        (nameBuf,) = mycursor.fetchall()
        print("Location: http://localhost:1000/ArabicMaster/game/games.html\n\n")
except:
    print("Location: http://localhost:1000/ArabicMaster/UserRegistration/login.html\n\n")

