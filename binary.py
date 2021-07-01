n=int(input("enter the number"))
q=n
binary=0
i=0
while q!=0:
    rem=q%2
    binary=binary+rem*(10**i)
    q=q//2
    i=i+1
    print("binary number",binary)