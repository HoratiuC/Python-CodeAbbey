#read file containing inputs - temperatures in Fahrenheit
with open('C:\\Users\\HoratiuC\\Documents\\inputs.txt','r') as f:
    l = f.read().split()

#how many temperatures will be converted
print("Will convert {} temperatures".format(l[0]))

#eliminate first element that doesn't need to be converted
l=l[1:]
print ("Fahrenheit:\n",l)

#define epmty list for results
celsius = []

#calculate Fahrenheit to Celsius conversion and round to the nearest integer
for i in l:
    i = (int(i)-32)*5/9
    if i<0:
        i = int(i-0.5)
    else:
        i = int(i+0.5)
    celsius.append(i)

print ("Celsius:\n", celsius)

#write the results to a different file
with open('C:\\Users\\HoratiuC\\Documents\\test.txt','a') as res:
    for j in celsius:
        res.write('{} '.format(str(j)))


