import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("300x300")

        self.choices = ["rock", "scissor", "paper"]

        self.label = tk.Label(root, text="Rock Paper Scissors Game")
        self.label.pack(pady=20)

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack()

    def play_game(self):
        ucount = 0
        ccount = 0

        for _ in range(3):
            user_input = simpledialog.askinteger("User Choice", "1. Rock\n2. Scissor\n3. Paper")
            if user_input is None:
                return

            user_choice = self.choices[user_input - 1]
            computer_choice = random.choice(self.choices)

            if user_choice == computer_choice:
                result = "Game Draw"
                ucount += 1
                ccount += 1
            elif (user_choice == "rock" and computer_choice == "scissor") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissor" and computer_choice == "paper"):
                result = "You win"
                ucount += 1
            else:
                result = "Computer wins"
                ccount += 1

            messagebox.showinfo("Round Result", f"User choice: {user_choice}\nComputer choice: {computer_choice}\nResult: {result}")

        if ucount == ccount:
            winner = "Game Draw"
        elif ucount > ccount:
            winner = "You win the game"
        else:
            winner = "Computer wins the game"

        play_again = messagebox.askyesno("Play Again?", f"Final Result: {winner}\nUser Score: {ucount}\nComputer Score: {ccount}\nDo you want to play again?")
        if play_again:
            self.play_game()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
