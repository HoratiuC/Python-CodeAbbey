#define function to calculate BMI
def bmi(weight, height):
    return weight/height**2

#read input file containing the data
with open('C:\\Users\\HoratiuC\\Documents\\inputs.txt') as f:
    l = f.read().split('\n')

#define empty list to append data except first element which represents the number of inputs
wt_ht = []
for i in l[1:]:
    wt_ht.append(i.split())

#define empty list to append results
res = []

#append the BMI results
for x in range(len(wt_ht)):
    a = bmi(float(wt_ht[x][0]),float(wt_ht[x][1]))
    res.append(a)

#define empty list to append the results in final format (strings)
final = []

for r in res:
    if r < 18.5:
        r = 'under'
        final.append(r)
    elif 18.5 <= float(r) < 25.0:
        r = 'normal'
        final.append(r)
    elif 25.0 <= float(r) < 30.0:
        r = 'over'
        final.append(r)
    else:
        r = 'obese'
        final.append(r)
    
#write results to file
with open('C:\\Users\\HoratiuC\\Documents\\test.txt','w') as t:
    print ("This program calculates BMI for {} people".format(l[0]))
    for fin in final:
        t.write('{} '.format(str(fin)))
    
