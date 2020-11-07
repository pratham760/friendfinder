# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:36:25 2020

@author: PRATHAM
"""



def sameele(l):
    n = len(l)
    c = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(l[i]==l[j]):
                c += 1
    print(c)            
    
if __name__=="__main__":
    l = list(map(int,input().rstrip().split()))
    sameele(l)    