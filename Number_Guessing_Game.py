""""
Number Geussing game 
----------------------------------------------------------------------------------------
"""

import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is no curently no high score, it's your for the taking")
    else:
        print(f"The current high score is {attempts_list} attempts")
def start_game():
    random_number = int(random.randint(1,10))
    print("Hell, traveler ! welcome to the game of guesses!")
    player_name = input("What is your name : \t")
    wana_play = input(f"Hi,{player_name}, would you like to play the guessing game ? (Enter Yes/No)\n")
    attempts = 0 
    show_score()
    while (wana_play.lower()== "yes"):
        try:
            guess = int(input("Pick a number between 1 and 10 : \t"))
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number with the given range : \t")
            elif guess == random_number:
                print("You got it! You Win")
                attempts += 1
                attempts_list.append(attempts)
                print(f"It took you {attempts} attempts ")
                play_again = input("would like to play again (Enter Yes/No) ? \t")
                attempts = 0
                show_score()
                random_number = int(random.randint(1,10))
                if play_again.lower() == 'no':
                    print("That's cool, have a good one ")
                    break
            elif random_number < guess:
                print("It's higher")    
                attempts += 1 
            elif random_number > guess:
                print("It's lower")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is no a valid value. try again.....?\t")
            print(f"{err}")
    else:
        print("That's cool. have a good one !")
if __name__ == "__main__":
    start_game()
