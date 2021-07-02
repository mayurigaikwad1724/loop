i=10
a=[]
while i>0:
    num=int(input("enter number: "))
    a.append(num)
    i=i-1
print(a)
n=int(input("enter the number: "))
j=9
c=0
while j>c:
    if n in a:
        print("yes")
        break
    else:
        print("no")
        continue
    c=c+1
i=i-1


