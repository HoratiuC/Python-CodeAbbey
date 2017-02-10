f=open("C:\\Users\\HoratiuC\\Documents\\numbers.txt",'r+')
nums = f.read().split('\n')

print ("This program calculates minimum of {} pairs of numbers".format(int(nums[0])))

l = nums[1:]

k=[]
for i in l:
    k.append(i.split())

answer=[]

for x in range(0,len(k)):
    min = int(k[x][0])
    if int(k[x][1])<min:
        res = int(k[x][1])
    elif int(k[x][2])<min:
        res = int(k[x][2])
    else: 
        res = min
    answer.append(res)

print (answer)
f.close()
    
   

    

    
       
   



