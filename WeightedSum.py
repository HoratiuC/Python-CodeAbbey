with open("C:\\Users\\HoratiuC\\Documents\\diverse\\prog\\inputs.txt",'r+') as f:
    l = f.read().split('\n')

print ("Sum of digits for {} numbers".format(int(l[0])))
a = int(l[0])

l = [i.split() for i in l[1:]]
l = [item for sublist in l for item in sublist]

res = []

for i in l:
    s = 0
    d = list(i)
    print (d)
    for j in range(len(d)):
        print ('j:',j)
        print ('d[j]:',d[j])
        print ('j+1:',j+1)
        s += int(d[j])*(j+1)
        print ('s:',s)
    res.append(str(s))
    
print (' '.join(res))
        



        
        



