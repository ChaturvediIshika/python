ls=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text,shift):
    ch=""
    for i in text:
        if i in ls:
            h=ls.index(i)
            if h+shift>25:
                ch=ch+ls[h+shift-26]
            else:
                ch=ch+ls[h+shift]
        else:
            ch+=i
    print(f"the encoded text is: {ch}")
def decrypt(text,shift):
    ch=""
    for i in text:
        if i in ls:
            h=ls.index(i)
            ch=ch+ls[h-shift]
        else:
            ch+=i
    print(f"the decoded text is: {ch}")
flag=True
while flag:
    dire=input("Type 'encode' to encrypt ;Type 'decode' to decrypt :\n")
    text=input("type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    if dire=="encode":
        encrypt(text,shift)
    else:
        decrypt(text,shift)
    a=input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if a=='no':
        flag=False
    else:
        flag=True
