#read the file which contains the pairs
f=open("C:\\Users\\HoratiuC\\Documents\\numbers.txt","r")
nums = f.read().split('\n')

#read the first element of the list, showing the number of pairs
print ("This program sums {} pairs of numbers".format(int(nums[0])))

#remove first element, only pairs remain
l = nums[1:]

#split the list
k=[]
for i in l:
    k.append(i.split())

sum=0
#sum of each pair will be appended to answer
answer=[]

for x in range(0,len(k)):
    sum = int(k[x][0])+int(k[x][1])
    answer.append(sum)

print (answer)
    
   

    

    
       
   



