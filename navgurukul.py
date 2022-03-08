i=0
while(i<=99):
    i=i+1
    if(i%3==0 and i%7==0):
        print("Navgurukul")
        continue
    elif(i%3==0):
        print("Nav")
        continue
    elif(i%7==0):
        print("Gurukul")
        continue
    else:
        print(i)