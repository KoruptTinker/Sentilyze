def analyzer():
    
    #importing positive words into a list
    
    positive_list=[]
    with open("./data/positive.txt", "r") as f:
        for line in f:
            positive_list.append((line))

    #importing negative words into a list


    negative_list=[]
    with open("./data/dnegative.txt", "r",encoding="ISO-8859-1") as f:
        for line in f:
            negative_list.append((line))



    #importing training set

    dataset=[]
    with open("./data/dataset.txt","r") as f:
        for line in f:
            dataset.append(f.readline())
        
        
    dataNum=[]
    i=0
    for i in range(len(dataset)):
        temp=  dataset[i]
        word_list=temp.split()
        k=word_list[-1]
        dataNum.append(k)



    #datapreprocessing 
        
        
    import nltk 
    import numpy as np
    import nltk
    import re
    import pandas as pd
    from nltk.stem.porter import PorterStemmer 
    ps=PorterStemmer()


    def stemmer(list):
        temp=[]
        for i in list:
            i=i.replace("\n","")
            temp.append(ps.stem(i))
        return temp

    positive_list=stemmer(positive_list)
    negative_list=stemmer(negative_list)

    def purify(list):
        i=0
        while i<len(list):
            list[i]=re.sub('[^a-zA-Z]',' ',str(list[i]))
            list[i]=list[i].lower()
            i=i+1
            
    def count(lst):
        neglist=[]
        poslist=[]
        num_neg=[]
        num_pos=[]
        final=[]
        i=0
        while i<len(lst):
            abc=(lst[i].split(" "))
            abc=stemmer(abc)
            neg=[word for word in list(abc) if (word) in negative_list]
            pos=[word for word in list(abc) if (word) in positive_list]
            neglist.append(neg)
            poslist.append(pos)
            num_pos.append(len(poslist[i]))
            num_neg.append(len(neglist[i]))
            final.append([num_pos[i],num_neg[i]])
            i+=1
        return final


    purify(dataset)
    final=count(dataset)

    def converttoarray(list):
        from numpy import array
        return array(list)

    def converttolist(array):
        tempo=[]
        for i in array:
            tempo.append(i)
        return tempo

    X=converttoarray(final)
    Y=converttoarray(dataNum)

    #training


    from sklearn.model_selection import train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

    from sklearn.linear_model import LinearRegression
    regressor=LinearRegression()
    regressor.fit(X_train,Y_train)

    Y_pred = regressor.predict(X_test)

    Y_pred=converttolist(Y_pred)
    average=sum(Y_pred)/len(Y_pred)

    def converttovalues(list):
        temp=[]
        for i in list:
            if(i>average):
                temp.append(1)
            else:
                temp.append(0)
        return temp

    Y_pred=converttovalues(Y_pred)
    Y_test=Y_test.tolist()
    cp=0
    wp=0
    for i in range(len(Y_pred)):
        if(int(Y_pred[i])==int(Y_test[i])):
            cp+=1
        else:
            wp+=1
        




    #Handeling real data
        
    data=(pd.read_csv('./data/dtweets.csv')).values.tolist()
    purify(data)
    data=count(data)
    data=converttoarray(data)
    a=converttolist(regressor.predict(data))
    a=converttovalues(a)
    aa=[0]
    i=0
    while i<len(a):
        aa.append(a[i])
        i=i+1
    data=converttoarray(aa) 
    np.savetxt("./data/danalysis.csv", data, delimiter=",")




        
        









        
        
            






        

        
        
        
        
        
            
            
            
            
        
        
        
        


