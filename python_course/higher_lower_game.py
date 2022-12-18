import random
ls=[
    {
        'name':'Yash Agrawal',
        'followers':189,
    },
    {
        'name':'Aastha Goyal',
        'followers':78,
    },
    {
        'name':'Aditya Arora',
        'followers':53,
    },
    {
        'name':'Anikate Agrawal',
        'followers':158,
    },
    {
        'name':'Aanaya Singh',
        'followers':158,
    },
    {
        'name':'Anjali Jain',
        'followers':66,
    },
    {
        'name':'Aryan Upadhyay',
        'followers':168,
    },
    {
        'name':'Ayush Sharma',
        'followers':253,
    },
    {
        'name':'Chhaya Chaudhary',
        'followers':105,
    },
    {
        'name':'Divyanshi Varshney',
        'followers':199,
    },
    {
        'name':'Garima',
        'followers':237,
    },
    {
        'name':'Harshit',
        'followers':550,
    },
    {
        'name':'kajal Rathore',
        'followers':58,
    },
    {
        'name':'Pradyumn Gupta',
        'followers':694,
    },
    {
        'name':'Prashant',
        'followers':81,
    },
    {
        'name':'Prateek',
        'followers':332,
    },
    {
        'name':'Sarthak Singh',
        'followers':217,
    },
    {
        'name':'Surendra Singh',
        'followers':24,
    },
    {
        'name':'Anwesha',
        'followers':341,
    },
    {
        'name':'Vishal Chauhan',
        'followers':222,
    },
    {
        'name':'Tanya Bansal',
        'followers':131,
    },
    {
        'name':'Jagrati Garg',
        'followers':125,
    },
    {
        'name':'Yugal Gautam',
        'followers':129,
    }
]
print('''
.__    .__       .__                  
|  |__ |__| ____ |  |__   ___________ 
|  |  \|  |/ ___\|  |  \_/ __ \_  __ \
|   Y  \  / /_/  >   Y  \  ___/|  | \/
|___|  /__\___  /|___|  /\___  >__|   
     \/  /_____/      \/     \/       
.__                              
|  |   ______  _  __ ___________ 
|  |  /  _ \ \/ \/ // __ \_  __ \
|  |_(  <_> )     /\  ___/|  | \/
|____/\____/ \/\_/  \___  >__|   
                        \/       
''')

def compare(c3,c4):
    if ls[c3]['followers']>ls[c4]['followers']:
        return 0
    else:
        return 1
def quiz(c1,c2):
    print(f"compare A: {ls[c1]['name']}")
    print('''
                    
    ___  ________    
    \  \/ /  ___/    
     \   /\___ \     
      \_//____  > /\ 
              \/  \/ 
    ''')
    print(f"Against B: {ls[c2]['name']}")
game=True
score=0
while game:
    c1=random.choice(range(len(ls)))
    c2=random.choice(range(len(ls)))
    quiz(c1,c2)
    st=input("Who has more followers? Type 'A' or 'B': ")
    if st=='A':
        q=compare(c1,c2)
    else:
        q=compare(c2,c1)
    if q==1:
        print(f"Sorry!! that's wrong. Your final score is {score}")
        game=False
    else:
        score+=1
        print(f"You are right! Your current score is {score}")
    
