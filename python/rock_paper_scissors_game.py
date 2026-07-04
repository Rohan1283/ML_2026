import random

def get_choices():
    player_choice = input("Enter the choice (rock, paper, scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])

    return {"player" : player_choice, "computer" : computer_choice}

def check_win(player, computer):
    print(f"You choose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer =="paper":
            return "Paper covers rock ! You Lose"
        else:
            return "rock crushed scissors ! You Win"
    elif player == "paper":
        if computer =="rock":
            return "Paper covers rock ! You Win"
        else:
            return "Scissors cuts paper ! You Lose"
    elif player == "scissors":
        if computer =="paper":
            return "Scissors cut Paper ! You Win"
        else:
            return "rock crushed scissors ! You Lose"


choice = get_choices()
# print(choice)

result = check_win(choice["player"], choice["computer"])
print(result)
