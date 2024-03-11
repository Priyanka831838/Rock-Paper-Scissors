from random import randint

print("rock...")
print("paper....")
print("scissor..")

player=input("your turn's:").lower()
rand_num=randint(0,2)

if rand_num==0:
    computer="rock"
elif rand_num==1:
    computer="paper"
else:
    computer="scissor"

print(f"computer plays {computer}")

if player==computer:
    print("It's a tie")

elif player=="rock":
    if computer=="scissor":
        print("player wins!!!!!")
    else:
        print("computer wins!!!!!")

elif player=="paper":
    if computer=="scissor":
       print("computer wins!!!!!")
    else:
       print("player wins!!!!!")

elif player=="scissor":
    if computer=="rock":
        print("computer wins!!!!!")
    else:
        print("player wins!!!!!")
   
else:
    print("please enter a valid move")