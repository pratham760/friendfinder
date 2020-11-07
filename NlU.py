# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:48:54 2019

@author: PRATHAM
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:04:23 2019

@author: PRATHAM
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:51:48 2019

@author: PRATHAM
"""

import Tweetdata 
import json
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from watson_developer_cloud.natural_language_understanding_v1 import CategoriesOptions
user_scname1= input("Enter the screen name of the user1:")
#user_scname2= input("Enter the screen name of the user2:")
tweets1=[]
#tweets2=[]
data_str1=''' '''
#data_str2=''' '''
extractdata(user_scname1,tweets1)
#extractdata(user_scname2,tweets2)
for i in tweets1:
    data_str1 = data_str1+i
    
#for i in tweets2:
 #   data_str2 = data_str2+i    
params = {'entities': EntitiesOptions(emotion=True,
                                      sentiment=True, 
                                      mentions=True,
                                      limit=2),
          'keywords': KeywordsOptions(emotion=True, 
                                      sentiment=True, 
                                      limit=2),
          'categories': CategoriesOptions()} 

profile1 = nlu_service.analyze(features=Features(**params),text=data_str1).get_result()
#profile2 = service.profile(data_str2,content_type='text/plain').get_result()
result1 = json.dumps(profile1,indent=2)
#result2 = json.dumps(profile2['personality'],indent=2)
#dic1 = {}
#dic2 = {}
#personality1 = profile1['values']
#personality2 = profile2['personality']
#for values in personality1:
#    dic1[values["name"]]=values["percentile"]
#for big5 in personality2:
#    dic2[big5["name"]]=big5["percentile"]    
    
print(result1)
#print(dic2)        