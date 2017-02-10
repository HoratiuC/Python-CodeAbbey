f=open("C:\\Users\\HoratiuC\\Documents\\numbers.txt",'r+')
nums = f.read().split('\n')

print ("This program calculates minimum of {} pairs of numbers".format(int(nums[0])))

l = nums[1:]

k=[]
for i in l:
    k.append(i.split())

answer=[]

for x in range(0,len(k)):
    if int(k[x][0])<int(k[x][1]):
        min = int(k[x][0])
    else:
        min = int(k[x][1])
    answer.append(min)

print (answer)
f.write(answer)
f.close()
    
   

    

    
       
   



