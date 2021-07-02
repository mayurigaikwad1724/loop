list1=[[2,9],[1,10],[3,7]]
list2=[]
i=0
count=0
while i<len(list1):
    list2.append(list1[i])
    list2.sort()
    count=count+1
    i=i+1
print(count)
print(list2)

