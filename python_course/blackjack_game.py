import random
print(''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/              ''')
def deal_cards():
    '''returns a radom card from the deck'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    """returns total score"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,dealer_score):
    if user_score==dealer_score:
        return "Draw"
    elif dealer_score==0:
        return "Lose, Opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif dealer_score>21:
        return "opponent went over. you win"
    elif user_score>dealer_score:
        return "you win"
    else:
        return "you lose"
def play_game():
    game_over=False
    user=[]
    dealer=[]
    for _ in range(2):
        user.append(deal_cards())
        dealer.append(deal_cards())
    while not game_over:
        user_score=calculate_score(user)
        dealer_score=calculate_score(dealer)
        print(f"your cards= {user}, your score= {user_score}")
        print(f"dealers first card={dealer[0]}")
        if user_score==0 or dealer_score==0 or user_score>21:
            game_over=True
        else:
            ch=input("Type 'y' to get another card, Type 'n' to pass: ")
            if ch=='y':
                user.append(deal_cards())
            else:
                game_over=True
    while dealer_score!=0 and dealer_score<17:
        dealer.append(deal_cards())
        dealer_score=calculate_score(dealer)
    print(f"Your final hand={user}, final score={user_score}")
    print(f"Dealers final hand={dealer}, dealer score={dealer_score}")
    print(compare(user_score,dealer_score))
while input("Do you want to play the blackjack game? Type 'y' or 'n': ")=='y':
    play_game()