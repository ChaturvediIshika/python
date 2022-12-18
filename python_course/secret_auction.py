logo='''               
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
                       '''
print(logo)
bidders={}
flag=True
while flag:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    bidders[name]=bid
    choice=input("are there any other bidders? type 'yes' or 'no': ")
    if choice=='no':
        flag=False
max=0
for i in bidders:
    if bidders[i]>max:
        max=bidders[i]
        q=i
print(f"The winner is {q} with a bid of ${max}")
