#Rock Paper Scissors
import random as r
options = ("Rock","Paper","Scissors")
running = True

while running:

    player = None
    computer = r.choice(options)
    
    while player not in options:
        
        player = input("Enter a choice (Rock, Paper or Scissors): ").capitalize()
        print("Invalid input")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("Rock smashes scissors! Player wins!")
    elif player == "Paper" and computer == "Rock":
        print("Paper covers rock! Player wins!")
    elif player == "Scissors" and computer == "Paper":
        print("Scissors cuts paper! Player wins!")
    else:
        print("Computer wins!(Player losses)")
    
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        running = False
        print("Thanks for playing!")
        