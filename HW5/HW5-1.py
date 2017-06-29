# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:57:11 2017

@author: Jacques Menard
"""
import re


#1b I found the most informative piece of data to be in the Average word length over 3.
#   Words relating to calling and texting appear much more often in spam. This makes sense
#   to me since spam ussually isnt nonsense, it has an agenda. Call, free, text, claim, mobile,
#   are all very prominent in the spam messages and show up a lot less often in non-spam.
def hamAndSpam(smsFilename):
    #dictionary fields for hamAndSpam\
    spamCount=0
    hamCount=0
    spam={}
    ham={}
    myFile=open(smsFilename,encoding='utf-8')
    myLines=[]
    for line in myFile:
        #attempts to filter out extra characters and split the line into individual lower case words
        line=re.sub('[\t]', ' ', line)
        for char in line:
            #I decided to include numbers as characters
            if(char.lower() not in "abcdefghijklmnopqrstuvwxyz0123456789'"):
                line.replace(char,"")
        line=line.replace(".","")
        line=line.replace(",","")
        line=line.strip()
        line=line.lower()
        line=line.split(" ")
        myLines.append(line)
    myFile.close()
    #builds a dictionary for spam and ham giving each "word" a frequency
    for line in myLines:
        if line[0]=="spam":
            spamCount+=1
            for word in line:
                if word not in spam:
                    spam[word]=1
                else:
                    spam[word]+=1
        else:
            hamCount+=1
            for word in line:
                if word not in ham:
                    ham[word]=1
                else:
                    ham[word]+=1
    top5spam=[]
    top5ham=[]
    #some extra cleaning of my dictionaries
    spam.pop('',None)
    ham.pop('',None)
    
    spam.pop('spam',None)
    ham.pop('ham',None)
    
    #creates a tuple list of the top 10 words in spam
    for key in spam:
        if(len(top5spam)==0):
            top5spam.append((spam[key],key))
        elif((len(top5spam)<10)):
            top5spam.append((spam[key],key))
 
            
        else:
            if(top5spam[9][0]<spam[key]):
                top5spam[9]=(spam[key],key)    
                
        top5spam.sort(reverse=True)
    
        #creates a tuple list of the top 10 words in ham
    for key in ham:
        if(len(top5ham)==0):
            top5ham.append((ham[key],key))
        elif((len(top5ham)<10)):
            top5ham.append((ham[key],key))
 
            
        else:
            if(top5ham[9][0]<ham[key]):
                top5ham[9]=(ham[key],key)    
                
        top5ham.sort(reverse=True)
    
    topBigHam=[]
    topBigSpam=[]
    #creates a tuple list of the top 10 words over 3 letters in spam
    for key in spam:
        if(len(topBigSpam)==0):
            if(len(key)>3):
                topBigSpam.append((spam[key],key))
        elif((len(topBigSpam)<10)):
            if(len(key)>3):
                topBigSpam.append((spam[key],key))
 
            
        else:
            if(topBigSpam[9][0]<spam[key]):
                if(len(key)>3):
                    topBigSpam[9]=(spam[key],key)    
                
        topBigSpam.sort(reverse=True)
    
        #creates a tuple list of the top 10 words over 3 letters in ham
    for key in ham:
        if(len(topBigHam)==0):
            if(len(key)>3):
                topBigHam.append((ham[key],key))
        elif((len(topBigHam)<10)):
            if(len(key)>3):
                topBigHam.append((ham[key],key))
 
            
        else:
            if(len(key)>3):
                if(topBigHam[9][0]<ham[key]):
                    topBigHam[9]=(ham[key],key)    
                
        topBigHam.sort(reverse=True)        
    #compare the average word lengths in ham and spam
    spamAverage=0
    mySum=0
    for key in spam:
        mySum+=len(key)
    spamAverage=mySum/len(spam)
    
    
        #compare the average word lengths in ham and spam
    hamAverage=0
    mySum=0
    for key in ham:
        mySum+=len(key)
    hamAverage=mySum/len(ham)
    
    print()
    print("Summary Information")
    print()
    print("Total number of spam messages:",spamCount)
    print("Total number of ham messages:",hamCount)
    print("Average word length in spam messages:",spamAverage)
    print("Average word length in non-spam messages:",hamAverage)
    print("List of 10 most used words in spam messages and their occurences:",top5spam)
    print("List of 10 most used words in non-spam messages and their occurences:",top5ham)
    print("List of 10 most used words in spam messages with a length greater then 3 and their occurences:",topBigSpam)
    print("List of 10 most used words in non-spam messages with a length greater then 3 and their occurences:",topBigHam)