from math import sqrt

def primelist(limit):
    li = [2,3,5,7]
    k=2
    a=6*k-1
    somme = 17
    while a<limit : 
        if is_prime(a,li):
            li.append(a)
            #print(len(li))
            somme = somme + a
        if a == 6*k+1:
            k+=1
            a=6*k-1
        elif a == 6*k-1:
            a=6*k+1
    print(somme)
    return li 

def is_prime(a,li):
  i=0
  prim = True
  while li[i] < (round(sqrt(a))+1):  
        if a%li[i] ==0:               
          prim = False        
        i +=1
  return prim

print("Entrez une limite")

a = int(input())

b= primelist(a)
