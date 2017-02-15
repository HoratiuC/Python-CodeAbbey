with open('C:\\Users\\HoratiuC\\Documents\\inputs.txt','r') as f:
    l = f.read().split()

print("Will convert {} temperatures".format(l[0]))

l=l[1:]
print ("Fahrenheit:\n",l)
celsius = []

for i in l:
    i = (int(i)-32)*5/9
    if i<0:
        i = int(i-0.5)
    else:
        i = int(i+0.5)
    celsius.append(i)

print ("Celsius:\n", celsius)

with open('C:\\Users\\HoratiuC\\Documents\\test.txt','a') as res:
    for j in celsius:
        res.write('{} '.format(str(j)))


