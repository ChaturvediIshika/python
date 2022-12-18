ls=list(map(int,input().split()))
q=ls
m=ls[0]
for i in ls:
    if m<i:
        m=i
print(f"the heightest score is ={m}")
print(max(ls))
print(min(ls))