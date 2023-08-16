import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do List')
        self.root.geometry('650x410+300+150')

        self.label = tk.Label(self.root, text='To-do List', font='Arial 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=tk.BOTH)

        self.label2 = tk.Label(self.root, text='ADD TASK', font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = tk.Label(self.root, text='TASKS', font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = tk.Listbox(self.root, height=9, bd=5, width=23, font='Arial 20 italic bold')
        self.main_text.place(x=250, y=100)

        self.text = tk.Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        self.load_tasks()

        self.add_button = tk.Button(self.root, text='ADD', font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=self.add_task)
        self.add_button.place(x=30, y=180)

        self.delete_button = tk.Button(self.root, text='DELETE', font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=self.delete_task)
        self.delete_button.place(x=30, y=220)

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

    def save_tasks(self):
        tasks = self.main_text.get(0, tk.END)
        with open('data.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')

    def add_task(self):
        content = self.text.get('1.0', tk.END).strip()
        if content:
            self.main_text.insert(tk.END, content)
            self.save_tasks()
            self.text.delete('1.0', tk.END)

    def delete_task(self):
        selected_indices = self.main_text.curselection()
        if selected_indices:
            for index in reversed(selected_indices):
                self.main_text.delete(index)
            self.save_tasks()

def main():
    root = tk.Tk()
    ui = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
