with open('17.txt') as f:
    a=[int(x) for x in f]
    print(a)
    count=0
    b=[]
    for i in a:
        if i%10==3: b.append(i)
    print(max(b))
    for i in range(len(a)-1):
        if abs(a[i]%10==3 and a[i+1]%10!=3) or abs(a[i]%10!=3 and a[i+1]%10==3):
            count=count+1
    print(count)
