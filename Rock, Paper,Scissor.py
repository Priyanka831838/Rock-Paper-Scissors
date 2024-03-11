print("rock...")
print("paper....")
print("scissor..")
player1=input("Player1 turn's:")
player2=input("Player2 turn's:")



if player1==player2:
    print("It's a tie")

elif player1=="rock":
    if player2=="scissor":
        print("Player1 wins!!!!!")
    elif player2=="paper":
        print("Player2 wins!!!!!")

elif player1=="paper":
    if player2=="scissor":
       print("Player2 wins!!!!!")
    elif player2=="rock":
       print("Player1 wins!!!!!")

elif player1=="scissor":
    if player2=="rock":
        print("Player2 wins!!!!!")
    elif player2=="paper":
        print("Player1 wins!!!!!")

    
else:
    print("something wrong")