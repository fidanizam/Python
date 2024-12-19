import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""
input_var = tk.StringVar()


entry = tk.Entry(root, textvariable=input_var, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)


button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

button_frame = tk.Frame(root)
button_frame.pack()

for row in button_texts:
    button_row = tk.Frame(button_frame)
    button_row.pack(expand=True, fill="both")
    for text in row:
        btn = tk.Button(button_row, text=text, font=("Arial", 18), width=4, height=2, relief=tk.GROOVE, bd=2)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)


root.mainloop()
