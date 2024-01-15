a=[3,3]
tgt=6
ans=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==tgt:
            print(i,j)
        else:
            pass
