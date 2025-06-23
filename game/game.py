
player = input("Player 1 (you): rock, paper or scissors? ").lower()
computer = input("Player 2 (computer): rock, paper or scissors? ").lower()
print("You chose:", player)
print("Computer chose:", computer)
if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
    print("You win!")
else:
    print("You lose!")