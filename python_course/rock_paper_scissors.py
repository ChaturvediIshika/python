import random
stone=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
q=[stone,paper,scissors]
a=int(input("enter your choice: 0 for rock, 1 for paper, 2 for scissors"))
print(q[a])
b=random.randint(0,2)
print("computer chose:")
print(q[b])
if a>=0 and a<=2:
    if a==0:
        if b==0:
            print("game tie")
        elif b==1:
            print("you won")
        else:
            print("you lose")  
    elif a==1:
        if b==0:
            print("you won")
        elif b==1:
            print("game tie")
        else:
            print("you lose")  
    else:
        if b==0:
            print("you lose")
        elif b==1:
            print("you won")
        else:
            print("game tie")  
else:
    print("wrong choice")
