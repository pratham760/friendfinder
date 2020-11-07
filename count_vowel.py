# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:25:41 2020

@author: PRATHAM
"""

def fuck(s,k):
    sub = s[0:k]
    n = len(s)
    mc = 0
    for i in range(1,n-k+1):
        if('a' in sub or 'e' in sub or 'i' in sub or 'o' in sub or 'u' in sub):
            c1 = sub.count('a')            
            c2 = sub.count('e')
            c3 = sub.count('i')
            c4 = sub.count('o')
            c5 = sub.count('u')
            c = c1 + c2 + c3 + c4 + c5
            if(mc < c):
                mc = c
        sub = s[i:i+k]
    print(mc)        
    
if __name__=="__main__":
    a = input("a string:") 
    k = int(input())
    fuck(a,k)