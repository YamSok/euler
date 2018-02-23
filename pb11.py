
#entrer la matrice
#li = [input().split() for i in range(3)]
#print(li)


def horizontal(matrice):      # prend en arg une ligne donc un element de li
    tab = []
    for j in range(len(matrice)):
        for i in range(len(matrice[0])-3):
            count = 1
            for j in range(i,4+i):
                if int(matrice[i][j]) == 0:
                    break
                else:
                    count = count*int(matrice[i][j])
            tab.append(count)
    return tab

def vertical(matrice):
    tab_v = []
    count_v = 1
    for i in range(len(matrice[0])):
        for j in range(len(matrice)-3):
            count_v = 1
            for k in range(j,4+j):
                print(matrice[j][i])
                if int(matrice[j][i]) == 0:
                    break
                else:
                    count_v = count_v*int(matrice[j][i])
            tab_v.append(count_v)
    return tab_v


#entrer la matrice
matrice = [input().split() for i in range(5)]
#matrice = [[int(d) for i in len(matrice)] for d in matrice[i]]

print(vertical(matrice))

#print(li)







