import random
choices = ['Rock', 'Paper','Scissors']
print("Rock! Paper! Scissors!")
comp = random.choice(choices)
print("THE GAME IS ABOUT TO BEGIN!!")
u=0
c=0
p = input("Do you wish to play")
while p=='Y' or p=='y':
    user = input("Choose from rock paper scissors ---> ")
    if comp=='Rock' and user=='Paper':
        u=u+1
    elif comp=='Rock' and user=='Scissors':
        c=c+1
    elif comp=='Rock' and user =='Rock':
        u = u+1
        c = c+1
    elif comp=='Paper' and user == 'Paper':
        u = u+1
        c = c+1
    elif comp=='Paper' and user == 'Rock':
        c = c+1
    elif comp=='Paper' and user =='Scissors':
        u = u+1
    elif comp=='Scissors' and user=='Scissors':
        u = u+1
        c = c+1
    elif comp=='Scissors' and user=='Rock':
        u = u+1
    else:
        c=c+1

if c>u:
    print("Sorry, You Loose")
elif c<u:
    print("Congratulations, You Win")
else:
    print("Its a Tie")
    

    
    
