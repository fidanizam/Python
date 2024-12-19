import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    global current_file
    text_area.delete(1.0, tk.END)
    current_file = None

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def exit_editor():
    if messagebox.askyesno("Exit", "Do you want to save changes before exiting?"):
        save_file()
    root.destroy()


root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

current_file = None


text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 14))
text_area.pack(fill=tk.BOTH, expand=True)


menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)


root.config(menu=menu_bar)

root.mainloop()
