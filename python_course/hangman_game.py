import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                    ''')
hangman=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
lives=6
ls=["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure",
"bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords",
"caliph","cobweb","cockiness","croquet","crypt","curacao","cycle",
"daiquiri","dirndl","disavow","dizzying","duplex","dwarves",
"embezzle","equip","espionage","exodus",
"faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny",
"gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess",
"haiku","haphazard","hyphen",
"iatrogenic","icebox","injury","ivory","ivy",
"jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo",
"kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack",
"larynx","lengths","lucky","luxury","lymph",
"marquis","matrix","megahertz","microwave","mnemonic","mystify",
"naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen",
"pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling",
"quartz","queue","quips","quixotic","quiz","quizzes","quorum",
"razzmatazz","rhubarb","rhythm","rickshaw",
"schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome",
"thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth",
"unknown","unworthy","unzip","uptown",
"vaporize","vixen","vodka","voodoo","vortex","voyeurism",
"walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern",
"xylophone",
"yachtsman","yippee","yoked","youthful","yummy",
"zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]
st=random.choice(ls)
l=len(st)
q=l
flag=1
blank=[]
for i in range(l):
    blank.append("_")
print(blank)
while q>0 and lives>0:
    ch=input("Guess a letter : ").lower()
    if ch in blank:
        print(f"You have already guessed {ch}")
        continue
    flag=1
    for i in range(l):
        if ch==st[i]:
            blank[i]=ch
            q-=1
            flag=0        
    if flag==1:
        print(f"You guessed {ch}: that is not in the word. You lose a life. ")
        lives-=1
        #print(hangman[lives])
    print(blank)
    print(hangman[lives])
if q==0:
    print("you win")
elif lives==0:
    print("you lose")
    print(st)
