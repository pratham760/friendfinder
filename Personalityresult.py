# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:49:26 2019

@author: PRATHAM
"""
import Tweetdata 
import json

user_scname1= input("Enter the screen name of the user1:")
user_scname2= input("Enter the screen name of the user2:")
tweets1=[]
tweets2=[]
data_str1=''' '''
data_str2=''' '''
extractdata(user_scname1,tweets1)
extractdata(user_scname2,tweets2)
for i in tweets1:
    data_str1 = data_str1+i
    
for i in tweets2:
    data_str2 = data_str2+i    

profile1 = service.profile(data_str1,content_type='text/plain').get_result()
profile2 = service.profile(data_str2,content_type='text/plain').get_result()
result1 = json.dumps(profile1['personality'],indent=2)
result2 = json.dumps(profile2['personality'],indent=2)
print(result1)
dic1 = {}
dic2 = {}
personality1 = profile1['personality']
personality2 = profile2['personality']
for big5 in personality1:
    dic1[big5["name"]]=big5["percentile"]
for big5 in personality2:
    dic2[big5["name"]]=big5["percentile"]    
    
print(dic1)
print(dic2)        