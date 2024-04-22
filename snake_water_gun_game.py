import random
# rock Paper scissors  or snake water Gun game
def gameWin(comp,you):
    # if two values are equal,declare tie!
    if comp==you:
       return None
    #check for all possible situation when computer choose 'S'
    elif comp=='s':
       if you=='w':
           return False
       elif you=='g':
           return True
       #check for all possible situation when computer choose 'W'
    elif comp=='w':
       if you=='s':
           return False
       elif you=='g':
           return True
       #check for all possible situation when computer choose 'g'
    elif comp=='g':
       if you=='s':
           return False
       elif you=='w':
           return True
print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)  # randint is using for  genrate random integer b/w 2 numbers

if randNo==1:
    comp='S'
elif randNo==2:
    comp='W'
elif randNo==3:
    comp='g'

you=input("Player's  Turn: Snake(s) Water(w) or Gun(g)?\n Your Turn:-")

a=gameWin(comp,you)
print(f"Comp chose {comp}")
print(f"You chose {you}")

if a==None:
    print("The Game is Tie!")
elif a:
    print("You Win..")
else:
    print("You Lose...")