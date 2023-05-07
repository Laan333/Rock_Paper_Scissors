from imgs.ascii_imgs import *
import random
all_items = [rock,paper,scissors]

user_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_answer = random.randint(0,2)
def draw_func():
    print(f"User choice:\n {all_items[user_answer]}")
    print(f"PC choice:\n {all_items[computer_answer]}")

if user_answer >= 3 or user_answer < 0:
    draw_func()
    print("You lose, Number not found")
elif user_answer == computer_answer:
    draw_func()
    print("Draw")
elif user_answer == 0 and computer_answer == 2:
    draw_func()
    print("You win")
elif user_answer == 2 and computer_answer == 0:
    draw_func()
    print("You lose")
elif user_answer > computer_answer:
    draw_func()
    print("You win")
elif computer_answer > user_answer:
    draw_func()
    print("You lose")
