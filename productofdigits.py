i=int(input("Enter the number:-"))
pro=1
while(i>0):
    pro=pro*(i%10)
    i=i//10
print("Product of digits=",pro)    