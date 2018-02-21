from math import sqrt
def triplett():
    for b in range(1,1001):    
        for a in range(1,999):
            if ( a+b+(sqrt(a**2 + b**2)) == 1000 ) :
                triplet = {"trip": a*b*sqrt(a**2 + b**2) ,"a":a,"b":b,"c":sqrt(a**2 + b**2)}
                
        
    return triplet


print(triplett())