import tkinter as tk
import random

def start_batting():
    global user_score, computer_score, batting
    user_score = 0
    computer_score = 0
    batting = "user"
    result_label.config(text="You are batting. Choose a number between 1 and 6.")
    user_input_entry.delete(0, tk.END)

def play_turn():
    global user_score, computer_score, batting

    try:
        user_input = int(user_input_entry.get())
        if user_input < 1 or user_input > 6:
            result_label.config(text="Invalid input. Choose a number between 1 and 6.")
            return
    except ValueError:
        result_label.config(text="Enter a valid number between 1 and 6.")
        return

    computer_input = random.randint(1, 6)
    computer_choice_label.config(text=f"Computer chose: {computer_input}")

    if batting == "user":
        if user_input == computer_input:
            batting = "computer"
            result_label.config(text=f"You are out! Your score: {user_score}. Now computer is batting.")
        else:
            user_score += user_input
            result_label.config(text=f"Your current score: {user_score}")
    else:  
        if user_input == computer_input:
            result_label.config(text=f"Computer is out! Computer's score: {computer_score}.")
            determine_winner()
        else:
            computer_score += computer_input
            result_label.config(text=f"Computer's current score: {computer_score}")
            if computer_score > user_score:
                result_label.config(text="Computer has won the game!")

    user_input_entry.delete(0, tk.END)

def determine_winner():
    if user_score > computer_score:
        result_label.config(text="Congratulations! You won the game.")
    elif user_score < computer_score:
        result_label.config(text="Computer won the game. Better luck next time!")
    else:
        result_label.config(text="It's a tie!")


root = tk.Tk()
root.title("Hand Cricket Game")
root.geometry("400x300")

user_score = 0
computer_score = 0
batting = "user"


instructions = tk.Label(root, text="Welcome to Hand Cricket!", font=("Arial", 14))
instructions.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer chose: -", font=("Arial", 12))
computer_choice_label.pack(pady=5)

user_input_entry = tk.Entry(root, font=("Arial", 12))
user_input_entry.pack(pady=5)

play_button = tk.Button(root, text="Play", font=("Arial", 12), command=play_turn)
play_button.pack(pady=5)

start_button = tk.Button(root, text="Start New Game", font=("Arial", 12), command=start_batting)
start_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)


root.mainloop()
