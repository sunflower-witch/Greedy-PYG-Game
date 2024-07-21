import random
import time


# Function to generate RGB escape codes
def rgb_escape_code(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


# Colors for text
WINNER_COLOR = rgb_escape_code(171, 157, 255)  # lilac for winner
RED_COLOR = rgb_escape_code(255, 157, 169)  # for crit failure (rolling 1)
FIRST_COLOR = rgb_escape_code(157, 255, 179)  # first player color
SECOND_COLOR = rgb_escape_code(157, 226, 255)  # second player color
TOTAL_COLOR = rgb_escape_code(255, 239, 157)  # second player color
RESET = "\033[0m"  # Reset color
UNDERLINE = '\033[4m'


def score_increase(a, total):
    continue_roll = True
    current = 0
    while continue_roll:
        if a == player1:
            print(f"{FIRST_COLOR}● Player {a}:{RESET}")
        else:
            print(f"{SECOND_COLOR}● Player {a}:{RESET}")
        roll = int(random.randint(1, 6))
        if roll == 1:
            print(f"{RED_COLOR}{UNDERLINE}You rolled 1.{RESET}[Total score: {TOTAL_COLOR}{total}{RESET}]")
            print(f"{RED_COLOR}Okay! Next player!{RESET}🐽")
            print("𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿")
            time.sleep(1)
            return 0
        else:
            current += roll
            print(f"{UNDERLINE}You rolled {roll}.{RESET} [Current score: {TOTAL_COLOR}{current}{RESET}] [Total "
                  f"without roll: {TOTAL_COLOR}{total}{RESET}]")
            time.sleep(1)
            print(f"Do you want to roll again? {FIRST_COLOR}{UNDERLINE}Y{RESET}{UNDERLINE}/{RED_COLOR}N{RESET}:")
            time.sleep(1)
            player_roll = input().strip().upper()
            if player_roll == "N":
                if total + current >= 100:
                    print("💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜")
                    print(f"🎉{WINNER_COLOR}Player ✨{a}✨ wins with{RESET} 🎉{TOTAL_COLOR}{total + current}{RESET}{WINNER_COLOR}🎉 points! Congrats!{RESET} 🎉")
                    print("💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜")
                    time.sleep(1)
                    return current
                else:
                    print(f"Okay! Your new total is: {TOTAL_COLOR}{total + current}{RESET}. Next player!")
                    print("𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿")
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
        print(f"Do you want to play again? {FIRST_COLOR}{UNDERLINE}Y{RESET}{UNDERLINE}/{RED_COLOR}N{RESET}:")
        user_answer = input().strip().upper()
        if user_answer == "N":
            print(f"💜 {WINNER_COLOR}Thank you for playing!{RESET} 💜")
            time.sleep(1)
            play_again = False


print("🐽🐽🐽🐽🐽🐽🐽🐽🐽🐽🐽")
print(f"{RED_COLOR} Welcome to Greedy Pyg!{RESET} ")
print("🐽🐽🐽🐽🐽🐽🐽🐽🐽🐽🐽")
time.sleep(1)
print("Please select the name for Player one:")
player1 = input().strip()
print("And now select the name for Player two:")
player2 = input().strip()
print(f"{RED_COLOR}Okay! Let's go!{RESET}🐽")
print("𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿𓇿")
play(player1, player2)
