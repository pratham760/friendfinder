def digit(n):
    s = str(n)
    l = list(map(int,s))
    ld = max(l)
    sd = min(l)
    r = ld*11+sd*7
    if(r>99):
        return r%100
    else:
        return r
    



if __name__=="__main__":
    n = int(input())
    l = list(map(int,input().rstrip().split()))
    dl = []
    for i in range(n):
        dl.append(digit(l[i]))
        
    el = []
    ol = []
    
    for i in range(n):
        if(i%2==0):
            el.append(dl[i]/10)
        else:
            ol.append(dl[i]/10)
        
    c = 0    
    for i in el:
        if(i is not 999 and el.count(i) > 1):
            if(el.count(i) is 2):
                c += 1
            else:
                c += 2
                
                    
        