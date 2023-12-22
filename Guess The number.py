import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess the number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

    def make_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.master.destroy()  # Close the app after correct guess
            elif guess < self.secret_number:
                messagebox.showinfo("Incorrect", "Too low! Try again.")
            else:
                messagebox.showinfo("Incorrect", "Too high! Try again.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()
