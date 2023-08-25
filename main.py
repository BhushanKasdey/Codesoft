import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.load_questions("quiz_questions.txt")

        self.score = 0
        self.current_question_index = 0

        self.welcome_label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Arial", 16))
        self.welcome_label.pack(pady=20)

        self.rules_label = tk.Label(root, text="Rules:\n1. Read each question carefully.\n2. Choose the correct option.\n3. Click 'Next' to continue.", justify="left")
        self.rules_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.option_vars = []
        self.option_buttons = []
        for _ in range(3):
            var = tk.IntVar()
            self.option_vars.append(var)
            option_button = tk.Checkbutton(root, variable=var)
            option_button.pack()
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.results_label = tk.Label(root, text="", font=("Arial", 14))
        self.results_label.pack(pady=20)

        self.load_question()

    def load_questions(self, filename):
        self.questions = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                question, options, answer = line.strip().split("||")
                options = options.split(",")
                self.questions.append({
                    "question": question,
                    "options": options,
                    "answer": answer
                })

    def load_question(self):
        self.clear_options()
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            self.question_label.config(text=self.current_question["question"])
            for i, option in enumerate(self.current_question["options"]):
                self.option_vars[i].set(0)
                self.option_buttons[i].config(text=option)
        else:
            self.display_results()

    def clear_options(self):
        for var in self.option_vars:
            var.set(0)

    def next_question(self):
        selected_options = []
        for var in self.option_vars:
            if var.get() == 1:
                selected_options.append(self.current_question["options"][self.option_vars.index(var)])

        if selected_options == [self.current_question["answer"]]:
            self.score += 1

        self.current_question_index += 1
        self.load_question()

    def display_results(self):
        self.welcome_label.destroy()
        self.rules_label.destroy()
        self.question_label.destroy()
        for button in self.option_buttons:
            button.destroy()
        self.next_button.destroy()

        self.results_label.config(text=f"Quiz completed!\nYour final score is: {self.score}/{len(self.questions)}")
        self.results_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
