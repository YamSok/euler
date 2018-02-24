file = open("number.txt")
tab = [int(f.strip('\n')) for f in file.readlines()]
print(''.join([str(sum(tab))[i] for i in range(10)]))