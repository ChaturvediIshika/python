import random
print("Welcome to the number guessing game.\nI am thinking of a number between 1 to 100.")
ch=random.choice(range(1,101))
def game(no):
    if no==ch:
        return 0
    elif no<ch:
        return -1
    else:
        return 1
def level(t):
    while t>0:
        print(f"You have {t} attempt left.")
        q=int(input("Make a guess:"))
        re=game(q)
        if re==0:
            print(f"You got it. The number was {ch}")
            break
        elif re==-1:
            print("Too low")
        else:
            print("Too high")
        t-=1
    if t==0:
        print(f"you have rum out of guesses. you lose. The number was {ch}")
st=input("Choose the difficulty level:Type 'easy' or 'hard': ")
if st=='easy':
    level(10)
else:
    level(5)