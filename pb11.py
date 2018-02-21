
def entrer_matrice():
    li = []
    a=1
    for i in range(3):
        a = input().split()
        li.append(a)
    print(li)

li = [input().split() for i in range(3)]
print(li)