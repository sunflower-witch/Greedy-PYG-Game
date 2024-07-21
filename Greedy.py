import random
import time


def score_increase(a, total):
    continue_roll = True
    current = 0
    while continue_roll:

        print(f"Player {a}:")
        roll = int(random.randint(1, 6))
        if roll == 1:
            print(f"You rolled 1. Your total score is {total}.")
            print(f"Okay! Your new total is: {total + current}. Next player!")
            print("------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------")
            time.sleep(1)
            return 0
        else:
            current += roll
            print(f"You rolled {roll}. Current score is {current} (Total without roll:{total}).")
            time.sleep(1)
            print(f"Do you want to roll again? Y/N:")
            time.sleep(1)
            player_roll = input().strip().upper()
            if player_roll == "N":
                if total + current >= 100:
                    print("💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜")
                    print(f"Player {a} wins with {total + current} points! Congrats!")
                    print("💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜")
                    time.sleep(1)
                    return current
                else:
                    print(f"Okay! Your new total is: {total+current}. Next player!")
                    print("------------------------------------------------------------------------------------")
                    print("------------------------------------------------------------------------------------")
                    time.sleep(1)
                    return current


def play(player1, player2):
    play_again = True
    while play_again:
        score1 = 0
        score2 = 0
        while score1 < 100 and score2 < 100:
            score1 += score_increase(player1, score1)
            if score1 >= 100:
                break
            score2 += score_increase(player2, score2)
            if score2 >= 100:
                break
        print("Do you want to play again? Y/N:")
        user_answer = input().strip().upper()
        if user_answer == "N":
            print("Thank you for playing! 💜")
            time.sleep(1)
            play_again = False


print("Hello, please select the name for Player one:")
player1 = input().strip()
print("And now select the name for Player two:")
player2 = input().strip()
play(player1,player2)
