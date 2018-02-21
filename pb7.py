from math import sqrt
def primelist(index):
    li = [2,3,5,7]
    i = li[len(li)-1] + 2
    while len(li)<index: 
        if is_prime(i,li):
            li.append(i)
            #print(len(li))
        i+=2                   #optimisable en rajoutant des conditions sur 
    #print(li)                 #l'incrémentation de i
    return li[len(li)-1]  #retourner seulement le tableau si besoin de versatilité


def is_prime(a,li):
  i=0
  prim = True
  while li[i] <= (round(sqrt(a))+1):  
        if a%li[i] ==0:               
          prim = False        
        i +=1
  return prim
            
      
print(primelist(10001))   






