i=0
sum=0
while(i<=10):
    n=int(input("Enter the weight:-"))
    sum=sum+n
    i=i+1
print(sum)    
average=sum/i
if(average%5==0):
    print("Average of number is multiple of 5")
else:
    print("Average of number is not a multiple of 5")    