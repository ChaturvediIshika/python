Menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "milk":0,
            "coffee":18
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":3
    }
}
w=300
c=100
m=200
money=0
def report(w,m,c,money):
    print(f"Water : {w}ml")
    print(f"Milk : {m}ml")
    print(f"Coffee : {c}g")
    print(f"Money : ${money}")
def make_coffee(t,w,m,c):
    if w<=Menu[t]['ingredients']['water']:
        print("Sorry there is not enough water.")
    elif  m<=Menu[t]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
    elif  c<=Menu[t]['ingredients']['coffee']:
        print("sorry there is not enough coffee.")
    else:
        print("Please insert coins:")
        quater=int(input("How many quaters? "))*0.01
        dimes=int(input("How many dimes? "))*0.05
        nickles=int(input("How many nickles? "))*0.1
        pennies=int(input("How many pennies? "))*0.25
        sum=quater+dimes+nickles+pennies
        if sum>Menu[t]['cost']:
            print(f"Here is ${round(sum-Menu[t]['cost'],2)} in change.")
            print(f"Here is your {t} enjoy!!")
            return 0
flag=True
while flag:
    a=1
    ch=input("Do you want a coffee? Type 'y' or 'n': ")
    if ch=='y':
        st=input("What would you like? (espresso/latte/cappuccino): ")
        if st=='report':
            report(w,m,c,money)
        else:
            a=make_coffee(st,w,m,c)
        if a==0:
            w=w-Menu[st]["ingredients"]["water"]
            c=c-Menu[st]["ingredients"]["coffee"]
            if st!='espresso':
                m=m-Menu[st]["ingredients"]["milk"]
            money+=Menu[st]["cost"]
    else:
        flag=False