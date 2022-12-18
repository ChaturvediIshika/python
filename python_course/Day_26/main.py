# with open("file_1.txt") as f1:
#     content_1=f1.readlines()
#     ls1=list(map(int,content_1))
#     print(ls1)
# with open("file_2.txt") as f2:
#     content_2=f2.readlines()
#     ls2=list(map(int,content_2))
#     print(ls2)
    
    
# result=[n for n in ls2 if n in ls1]

# print(result)

# string="my name is ishika chaturvedi."
# ls=string.split()
# result={n:len(n) for n in ls}
# print(result)

temp={
    "monday":12,
    "tuesday":14,
    "wednesday":15,
    "thursday":14,
    "friday":21,
    "staurday":22,
    "sunday":24
}
result={key:value*9/5+32 for (key,value) in temp.items()}
print(result)