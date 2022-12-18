import random
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')']
print("Welcome to the password generator!!")
s=int(input("How many small letters would you like in your password?\n"))
c=int(input("How many capital letters would you like in your password?\n"))
n=int(input("How many numbers would you like in your password?\n"))
sy=int(input("How many symbols would you like in your password?\n"))
ch=[]
for i in range(s):
    ch.append(random.choice(small))
for j in range(c):
    ch.append(random.choice(capital))
for k in range(n):
    ch.append(random.choice(number))
for l in range(sy):
    ch.append(random.choice(symbol))
str(random.shuffle(ch))
password=""
for char in ch:
    password=password+char
print(f"Your password is: {password}")