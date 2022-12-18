ls=list(map(int,input().split()))
sum=0
l=len(ls)
for i in ls:
    sum=sum+i
av=sum//l
print(av)