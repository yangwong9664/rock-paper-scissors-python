import random
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

rockArt = """\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n"""

paperArt = """\n
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n"""

scissorsArt = """\n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n"""

fuckYou = """\n
( ︶︿︶)_╭∩╮\n"""


choices = {
    0: "rock",
    1: "paper",
    2: "scissors",
    -1: "fuck you"
}

playerChoice = ""
playerChoiceAsInt = 0

computerChoice = random.randrange(0, 3)


def print_art(choice):
    if choice == 0:
        print(rockArt)
    elif choice == 1:
        print(paperArt)
    elif choice == 2:
        print(scissorsArt)
    else:
        print(fuckYou)


def calc(player, computer):
    if player == -1:
        print("Alright... calm down... you win...")
    elif player == computer:
        print("DRAW")
    elif (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
        print("YOU LOSE")
    else:
        print("YOU WIN")


while True:
    while playerChoice not in choices.values():
        x = input("\nChoose rock, paper or scissors\n")
        clearConsole()
        if x in choices.values():
            playerChoice = x
            for key, value in choices.items():
                if value == playerChoice:
                    playerChoiceAsInt = key

            print("\nYou chose: {}".format(playerChoice))
            print_art(playerChoiceAsInt)
            print("Computer chose: {}".format(choices.get(computerChoice)))
            print_art(computerChoice)

            calc(playerChoiceAsInt, computerChoice)
            playerChoice = ""

            break
        else:
            print("Try again.")
