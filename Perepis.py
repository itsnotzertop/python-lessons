f = open('Perepis.txt','r')
summ = 0
minn =int(input())
maxx =int(input())
for i in f:
    data = i[len(i)-5::]
    if minn<int(data) < maxx:
        base = i.split()
        summ +=1
        print(base[2],base[3])
print(summ)