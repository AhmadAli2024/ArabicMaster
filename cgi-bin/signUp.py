#! /usr/bin/python3

#print("Content-type: text/html\n\n")

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
mycursor = mydb.cursor()

form = cgi.FieldStorage()

firstName = form["firstNameInput"].value
lastName = form["lastNameInput"].value
email = form["emailInput"].value
userName = form["Username"].value
password = hashlib.sha512(form["passwordInput"].value.encode()).hexdigest()

mydb.cursor().execute(f"INSERT INTO users(firstName,lastName,email,userName,password) Values(\"{firstName}\",\"{lastName}\",\"{email}\",\"{userName}\",\"{password}\")")

mydb.commit()

print("Location: http://localhost:1000/ArabicMaster/game/games.html\n\n")
