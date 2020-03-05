'''API support for Sentilyzer.
@author: Brijesh Kumar'''
import tweepy
import csv
import re
import analyzer as an
import os
import pandas as pd
import queryFetch as QF
import mysql.connector 
api=""
result=""
tweets=[]
f=""
db=""
myc=""
resultF=0

#Function for API Connection.
def getAPIConnection():
    #Twitter authorization keys. (DO NOT EDIT THIS CODE)
    consumer_key= 'QvWyxQ2KymChGoRa0aJOqxrXi'
    consumer_secret='WQHhC3zEcew7VSrcP0a4rX2iiexE84bXAavxDNQbCyAwotFeY2'
    access_token= '805688951713517572-WanXOPfckOKD4gsvZMeuwBQ58Ne8jdJ'
    access_token_secret='1IlfsRyYBAaxKknWaZvsP0Ny4CLnMGXQ84ydvj4SIJX2o'
    #API Connection
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    api= tweepy.API(auth)
    # AUTH end

def storeDB():
        global db
        global myc
        global resultF
        db=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="sentilyzer"
    )
        myc=db.cursor()
        flag="True"
        myc.execute("INSERT INTO results (result,flag) VALUES (%s, %s)", (resultF, flag))
        db.commit()

#Function to generate list containing tweets.
def getList():
        global tweets
        global result
        result=re.sub(r"\n","",result)
        tweets.append(result)

#Function to create CSV from list generated.
def getCSV():
        global tweets
        global f
        with open("./data/dtweets.csv",'w+') as f:
                twriter=csv.writer(f)
                twriter.writerow("l")
                twriter.writerows([[item] for item in tweets])

#Converting data into user readable info.
def getAnalysis():
        global resultF
        positivity=0
        with open("./data/danalysis.csv") as f:
                analysisR=csv.reader(f)
                analysisList=[e[0].strip().split(",") for e in analysisR if e]
        for i in (analysisList):
                if(analysisList.index(i)!=0):
                        positivity+=1
        positivityPercent= (positivity/(len(analysisList)-1))*100
        print("Positivity Percentage : "+str('{0:.2f}'.format(positivityPercent))+" %")
        resultF=int(positivityPercent)

#Function to fetch tweets from hashtag.
def fetchTweetsByHash():
    maxTweets=100
    getAPIConnection() #Requesting API Connection.
    global api
    searchQuery=QF.getHash()
    langPref="en"
    count=0
    global result
    tweetResFinal=tweepy.Cursor(api.search,searchQuery,langPref,tweet_mode="extended")
    for tweet in tweetResFinal.items(maxTweets):
            temp=tweet.full_text
            #Removal of unwanted characters.
            linkRemoval = re.sub(r"http\S+", "", temp)
            hashRemoval= re.sub(r"#\S+","",linkRemoval)
            for character in (hashRemoval):
                    if(ord(character)>=127):
                            character=""
            
            utfRemoval= hashRemoval.encode('ascii', 'ignore').decode('ascii')
            result=re.sub(r"@\S+","",utfRemoval)
            print('-----')
            getList()
            count+=1
    getCSV()
    global f
    f.close()
    an.analyzer()
    os.remove("./data/dtweets.csv")
    getAnalysis()
    os.remove("./data/danalysis.csv")
    storeDB()

#Function to fetch tweets using Twitter Handle of the User
def fetchTweetsByUser():
        global f
        getAPIConnection()
        max_tweets=100
        count=0
        userID=QF.getUser()
        global result
        userTimeline=api.user_timeline(userID)
        for tweet in userTimeline:
            temp=tweet.text
            #Removal of unwanted characters.
            linkRemoval = re.sub(r"http\S+", "", temp)
            hashRemoval= re.sub(r"#","",linkRemoval)
            for character in (hashRemoval):
                    if(ord(character)>=127):
                            character=""
            
            utfRemoval= hashRemoval.encode('ascii', 'ignore').decode('ascii')
            result=re.sub(r"@\S+","",utfRemoval)
            print("--------")
            getList()
            count+=1
        getCSV()  
        f.close()
        an.analyzer()
        os.remove("./data/dtweets.csv")
        getAnalysis()
        os.remove("./data/danalysis.csv")
        storeDB()
