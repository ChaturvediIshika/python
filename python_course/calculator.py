def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def multi(a,b):
    return a*b
def mod(a,b):
    return a%b
a=int(input("What's the first number?: "))
flag=True
while flag:
    print('''
    +
    -
    *
    /
    %''')
    op=input("pick an operator: ")
    b=int(input("What's your second number?: "))
    if op=='+':
        result=add(a,b)
    elif op=='-':
        result=sub(a,b)
    elif op=='*':
        result=multi(a,b)
    elif op=='/':
        result=div(a,b)
    elif op=='%':
        result=mod(a,b)
    print(f"{a} {op} {b} = {result}")
    ch=input(f"Type 'y'to continue calculating with {result}, or or type 'n' to start a new calculation.")
    if ch=='y':
        a=result
    else:
        flag=False
