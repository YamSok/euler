
start = 1
tab = []
tab2 = []
while start < 10**6:
    n = start
    i = 0
    while n != 1:
        if n in tab2:
            break
            
        else: 
            if n%2 == 0:
                n = n/2
            else:
                n = 3*n+1
            i +=1
    tab.append(i)
    tab2.append(start)
    start +=1

print(tab2[tab.index(max(tab))])