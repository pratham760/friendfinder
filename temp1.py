# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:11:10 2019

@author: PRATHAM
"""

import csv
csv_columns=['User_Name','Openness','Conscientiousness','Extraversion','Agreeableness','Emotional range']
   

import Tweetdata 
import json
last_data=[]
total_user = int(input("Enter the total number of user:"))
for i in range(total_user):
    user_scname1= input("Enter the screen name of the user:")
    tweets1=[]
    data_str1=''' '''
    extractdata(user_scname1,tweets1)
    for i in tweets1:
       data_str1 = data_str1+i 
       
    profile1 = service.profile(data_str1,content_type='text/plain').get_result()
    result1 = json.dumps(profile1['personality'],indent=2)
    dic1 = {}
    personality1 = profile1['personality']
    dic1['User_Name']=user_scname1
    for big5 in personality1:
        dic1[big5["name"]]=big5["percentile"] 
    last_data.append(dic1)    
    
    
with open('personality.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in last_data:
        writer.writerow(data)
         