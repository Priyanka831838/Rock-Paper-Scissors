from random import randint
player_wins=0
computer_wins=0



def display_header():
    print(f"Player Score: {player_wins}, Computer Score: {computer_wins}")
    print("rock...")
    print("paper....")
    print("scissor..")

def computer_move():
    rand_num=randint(0,2)

    if rand_num==0:
        computer="rock"
    elif rand_num==1:
        computer="paper"
    else:
        computer="scissor"


def winner(player,computer):
    global player_wins
    global computer_wins
    if player==computer:
        print("It's a tie")

    elif player=="rock":
        if computer=="scissor":
            print("player wins!!!!!")
            player_wins=player_wins+1
        else:
            print("computer wins!!!!!")
            computer_wins=computer_wins+1

    elif player=="paper":
        if computer=="scissor":
            print("computer wins!!!!!")
            computer_wins=computer_wins+1
        else:
            print("player wins!!!!!")
            player_wins=player_wins+1

    elif player=="scissor":
        if computer=="rock":
            print("computer wins!!!!!")
            computer_wins=computer_wins+1
        else:
            print("player wins!!!!!")
            player_wins=player_wins+1
    
    else:
        print("please enter a valid move")


def start_game(winning_score):
    while player_wins<winning_score and computer_wins<winning_score:
        display_header()

        player=input("(enter your choise):").lower()
        if player=="quit" or player=="q":
            break
        computer=computer_move()
        winner(player,computer)

def display_winner():
    if player_wins>computer_wins:
        print("CONGRATS, YOU WON")
    elif player_wins<computer_wins:
        print("OHHHH NO!  COMPUTER WON")
    else:
        print("its a tie")


start_game(3)
display_winner()