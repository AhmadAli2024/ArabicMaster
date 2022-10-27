import mysql.connector
from urllib import request
from urllib.request import Request, urlopen
import struct
import threading

URL = "https://dictapi.alsharekh.org/result/rpopsearch?id="

#mysql connector
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fgs20228",
        port = "3305",
        )
mycursor = mydb.cursor()

def createUser(database, name):
    mycursor.execute("CREATE USER "+name)
    mycursor.execute("GRANT ALL PRIVILEGES ON words.* TO "+name)
    tempdb = mysql.connector.connect(
            host = "localhost",
            user = name,
            port = "3305",
            database = "words"
            )
    return tempdb

def deleteUser(database, name):
    database.cursor().execute("DROP USER "+name)

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter,finalA,finalED,finalAD,db):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.finalA = []
        self.finalED = []
        self.finalAD = []
        self.db = db

    def getWords(self,arr):
        for i in arr:
            jsonFile = Request(URL+str(i), headers={"User-Agent": "Mozilla/5.0"})
            jsonFile = urlopen(jsonFile).read()
            arabicWord = jsonFile[jsonFile.find(b"\x6e\x61\x6d\x65")+7:]
            arabicWord = arabicWord[0:arabicWord.find(b"\x22")]
            englishD = jsonFile[jsonFile.find(b"\x65\x6e\x67\x6c\x69\x73\x68\x4e\x61\x6d\x65")+14:]
            englishD = englishD[0:englishD.index(b"\x22")]
            arabicD = jsonFile[jsonFile.find(b"\x73\x65\x6e\x73\x65\x22\x3a\x22")+8:]
            arabicD = arabicD[0:arabicD.index(b"\x22")]
            if(arabicWord.decode() == "ull"):
                continue;
            try:
                self.db.cursor().execute("INSERT INTO WordTable(ID,Word,ArabicD,EnglishD) Values("+str(i)+",\""+arabicWord.decode()+"\",\""+arabicD.decode()+"\",\""+englishD.decode()+"\")")
            except:
                continue

    def run(self):
        print("Starting"+self.name)
        self.getWords(self.counter)
        try:
            self.db.commit()
        except:
            pass



NumberArr = []
tempNumberArr = []
#91005
tempCounter = int(10005/250)
for i in range(0,10006):
    tempNumberArr.append(i)
    if(i%tempCounter == 0):
        NumberArr.append(tempNumberArr)
        tempNumberArr = []
NumberArr[0].extend(tempNumberArr)

threads = []

for i in range(0,250):
    threads.append(myThread(i,"thread"+str(i),NumberArr[i],[],[],[],createUser(mydb,"thread"+str(i))))

for j in threads:
    j.start()


for j in threads:
    j.join()
        

print("done")

mydb.commit()
print("uploaded")
