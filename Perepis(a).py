f = open('Perepis.txt','r')
summ = 0
for i in f:
    data = i[len(i)-5::]
    if int(data) < 1978:
        base = i.split()
        summ +=1
        print(base[2],base[3])
print(summ)