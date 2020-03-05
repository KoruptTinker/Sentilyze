#@author: Brijesh Kumar
import mysql.connector
mydb=""
mycursor=""
searchQ=""
def getDBConnection():
    global mydb
    global mycursor
    global searchQ
    mydb=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="sentilyzer"
    )
    mycursor=mydb.cursor()
    mycursor.execute("SELECT search FROM searches ORDER BY ID DESC LIMIT 1")
    searchQ=mycursor.fetchone()

    
def getHash():
    getDBConnection()
    global searchQ
    temp=searchQ
    for i in temp:
        if(temp.index(i)==0):
            searchQ=i
    print(searchQ)
    searchQ="#"+searchQ
    searchQ=searchQ +" -filter:retweets"
    print(searchQ)
    return searchQ


def getUser():
    global searchQ
    getDBConnection()
    temp=searchQ
    for i in temp:
        if(temp.index(i)==0):
            searchQ=i
    return searchQ
