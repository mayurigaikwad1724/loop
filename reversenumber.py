i=int(input("Enter the nunber:-"))
num=0
while(i>0):
    num=(num*10)+i%10
    i=i//10
print("Reverse numbe=",num) 
