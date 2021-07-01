i=7
j=1
while i>=1:
    a=" "*j+"*"*i+" "*j
    print(a)
    i=i-2
    j=j+1
i=1
j=4
while i>=1:
    a=" "*j+" "*i+" "*j
    print(a)
    i=i+2
    j=j-1
    if i>7:
        break