# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:46:37 2020

@author: PRATHAM
"""

def sameele(l):
    n = len(l)
    c = 0
    for i in range(0,n-1):
        co = 0
        if(l[i] is not 0):
            for j in range(i+1,n):
                if(l[i]==l[j]):
                    co += 1
                    l[j] = 0
            for k in range(co,0,-1):
                c += k
    print(c)            
    
if __name__=="__main__":
    l = list(map(int,input().rstrip().split()))
    sameele(l)    