import random
choices = ('rock','paper','seissor')
print("rock")
print("paper")
print("seissor")
while True:
    player = input("Choose Any One:")
    computer = random.choice(choices)
    print("Your choice is:",player)
    print("Computer choice is:",computer)
    if player != "paper" and player != "rock" and player != "seissor":
        print("You entered wrong choice!")
    elif player == computer:
        print("Match Tie!")
    elif (player == "rock" and computer == "seissor"):
        print("You Win!")
    elif (player == "paper" and computer == "rock"):
        print("You Win!")
    elif (player == "seissor" and computer == "paper"):
        print("You Win!")
    else:
        print("You Lost!")
        print("Better Luck Next Time!")
    player = input("Do you want to continue (y/n) : ")
    if player == "n":
        break
    elif player == "y":
        continue
    else:
        print("Enter valid option!")
    player = input("Do you want to continue (y/n) : ")
print("See you Again!")