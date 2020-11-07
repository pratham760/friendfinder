# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:43:16 2020

@author: PRATHAM
"""

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
print(profile1)
