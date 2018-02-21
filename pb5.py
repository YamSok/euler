def pgcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a


def ppcm(a,b):
  if (a==0) or (b==0):
    return 0 
  else:
    return (a*b)/pgcd(a,b)




def smallestmultiple():
    p=1
    for i in range(1,19):
        p = ppcm(ppcm(i,i+1),p)
    return p
  
print(smallestmultiple())
