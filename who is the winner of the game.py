from random import randint

player_win=0
computer_win=0
winning_score=3

while player_win<winning_score and computer_win<winning_score:
    print(f"Player Score: {player_win}, Computer Score: {computer_win}")
    print("rock...")
    print("paper....")
    print("scissor..")

    player=input("your turn's:").lower()
    if player=="quit" or player=="q":
        break
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
            player_win=player_win+1
        else:
            print("computer wins!!!!!")
            computer_win=computer_win+1

    elif player=="paper":
        if computer=="scissor":
            print("computer wins!!!!!")
            computer_win=computer_win+1
        else:
            print("player wins!!!!!")
            player_win=player_win+1

    elif player=="scissor":
        if computer=="rock":
            print("computer wins!!!!!")
            computer_win=computer_win+1
        else:
            print("player wins!!!!!")
            player_win=player_win+1
    
    else:
        print("please enter a valid move")


print(f"FINAL SCORE----Player Score: {player_win}, Computer Score: {computer_win}")
if player_win>computer_win:
    print("CONGRATS, YOU WON")
elif player_win<computer_win:
    print("OHHHH NO!  COMPUTER WON")
else:
    print("its a tie")
