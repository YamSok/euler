
#entrer la matrice
#li = [input().split() for i in range(3)]
#print(li)
import time

def horizontal(matrice):      # prend en arg une ligne donc un element de li
    tab = []
    for i in range(len(matrice)):
        for j in range(len(matrice[0])-3):
            count = 1
            for k in range(4):
                if int(matrice[i][j+k]) == 00:
                    break
                else:
                    count = count*int(matrice[i][j+k])
            tab.append(count)
    return tab

def vertical(matrice):
    tab_v = []
    for i in range(len(matrice[0])):
        for j in range(len(matrice)-3):
            count_v = 1
            for k in range(4):
                if int(matrice[j][i]) == 00:
                    break
                else:
                    count_v = count_v*int(matrice[j+k][i])
            tab_v.append(count_v)
    return tab_v

def diagonal(matrice):   # dans l'autre sens
    tab_d = []
    for i in range(len(matrice[0])-3):
        for j in range(len(matrice)-3):
            count_d = 1
            for k in range(4):
                if int(matrice[j][i]) == 00:
                    break
                else:
                    count_d =count_d*int(matrice[j+k][i+k])
            tab_d.append(count_d)
    return tab_d

def diagonale_inv(matrice):
    tab_d = []
    l = len(matrice[0])-1
    for i in range(0,len(matrice[0])-3):
        for j in range(0,len(matrice)-3):
            count_d = 1
            for k in range(4):
                if int(matrice[l-j-k][i+k]) == 00:
                    break
                else:
                    count_d =count_d*int(matrice[l-j-k][i+k])
            tab_d.append(count_d)
    return tab_d


matrice = [input().split() for i in range(20)]

tab = []
tab.append(max(diagonal(matrice)))
tab.append(max(diagonale_inv(matrice)))
tab.append(max(vertical(matrice)))
tab.append(max(horizontal(matrice)))

maxi = max(tab)
print("#########################")
print("produit max : ",maxi)

start_time = time.time()
print("My program took", time.time() - start_time, "to run")

#print(li)




