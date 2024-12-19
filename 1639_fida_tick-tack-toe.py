import tkinter as tk
from tkinter import messagebox

current_player = "X"  
board = [None] * 9  
buttons = []  

def on_click(index):
    global current_player

    if board[index] is None:  
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif None not in board:  
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This tile is already taken!")

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def reset_board():
    global board, current_player
    board = [None] * 9
    for button in buttons:
        button.config(text="")
    current_player = "X"  

window = tk.Tk()
window.title("Tic-Tac-Toe")

for i in range(9):
    button = tk.Button(window, text="", font=("Arial", 20), height=2, width=5,
                       command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

window.mainloop()
