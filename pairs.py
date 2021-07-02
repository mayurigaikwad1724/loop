list_1=[1,1,2,4,3,4,3,4,4,3]
i=0
a=[]
b=[]
while i<len(list_1):
    count=0
    m=list_1[i]
    j=0
    while j<len(list_1):
        n=list_1[j]
        if m==n:
            b.append(n)
            count=count+1
        j=j+1
    k=0
    while k<len(list_1):
        if m not in a:
            a.append(m)
            print(m,"is",count)
        k=k+1
    i=i+1