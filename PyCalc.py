import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")
        self.master.resizable(False, False)

        self.entry = tk.Entry(master, font=('Arial', 20), bd=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        style = ttk.Style()
        style.configure("TButton", font=('Arial', 18))

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('^', 5, 1), ('√', 5, 2), ('%', 5, 3)
        ]

        for (text, row, column) in buttons:
            button = ttk.Button(master, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, sticky="nsew")
            button.bind("<Enter>", lambda event, b=button: b.config(style="TButton"))
            button.bind("<Leave>", lambda event, b=button: b.config(style="TButton"))

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(5, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)

    def button_click(self, value):
        if value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif value == "C":
            self.entry.delete(0, tk.END)
        elif value == "^":
            self.entry.insert(tk.END, "**")
        elif value == "√":
            try:
                result = eval(self.entry.get())
                if result >= 0:
                    result = round(result ** 0.5, 10)
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(result))
                else:
                    messagebox.showerror("Error", "Cannot calculate square root of a negative number")
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()