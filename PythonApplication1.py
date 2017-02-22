def bmi(weight, height):
    return weight/height**2

a = bmi(80,1.73)

def grades(n):
    if n < 18.5:
        print ("Underweight")
    elif 18.5 <= n < 25.0:
        print ("Normal")
    elif 25.0 <= n < 30.0:
        print ("Overweight")
    else:
        print ("Obesity")

with open('C:\\Users\\HoratiuC\\Documents\\inputs.txt') as f:
    l = f.read().split('\n')



wt_ht = []
for i in l[1:]:
    wt_ht.append(i.split())

res = []


for x in range(len(wt_ht)):
    a = bmi(float(wt_ht[x][0]),float(wt_ht[x][1]))
    res.append(a)

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
    
with open('C:\\Users\\HoratiuC\\Documents\\test.txt','w') as t:
    print ("This program calculates BMI for {} people".format(l[0]))
    for fin in final:
        t.write('{} '.format(str(fin)))
    



