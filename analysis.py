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
    consumer_key= ''
    consumer_secret=''
    access_token= ''
    access_token_secret=''
    #API Connection
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    api= tweepy.API(auth)
    # AUTH end

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
        return resultF

#Function to fetch tweets from hashtag.
def fetchTweetsByHash(hash):
    maxTweets=100
    getAPIConnection() #Requesting API Connection.
    global api
    searchQuery=hash
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
    res=getAnalysis()
    os.remove("./data/danalysis.csv")
    return res

#Function to fetch tweets using Twitter Handle of the User
def fetchTweetsByUser(userName):
        global f
        getAPIConnection()
        max_tweets=100
        count=0
        userID=userName
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
        res=getAnalysis()
        os.remove("./data/danalysis.csv")
        return res