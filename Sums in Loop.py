f=open("C:\\Users\\HoratiuC\\Documents\\numbers.txt","r")
nums = f.read().split('\n')

print ("This program sums {} pairs of numbers".format(int(nums[0])))

l = nums[1:]

k=[]
for i in l:
    k.append(i.split())

sum=0
answer=[]

for x in range(0,len(k)):
    sum = int(k[x][0])+int(k[x][1])
    answer.append(sum)

print (answer)
    
   

    

    
       
   



