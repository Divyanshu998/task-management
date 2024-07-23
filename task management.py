import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TaskManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management App")
        self.root.configure(background="#f0f1f0")

        self.tasks = []

        # Create GUI components
        self.label = tk.Label(root, text="Welcome to the Task Management App!", font=("Times New Roman", 18, "bold"), fg="#00698f", bg="#f0f0f0")
        self.label.pack(pady=20)

        self.total_task_label = tk.Label(root, text="Enter how many tasks you want to add:", font=("Times New Roman", 12), fg="#333", bg="#f0f0f0")
        self.total_task_label.pack()
        self.total_task_entry = tk.Entry(root, width=20, font=("Times New Roman", 12), fg="#333", bg="#fff")
        self.total_task_entry.pack()

        self.add_tasks_button = tk.Button(root, text="Add Tasks", command=self.add_tasks, font=("Times New Roman", 12), fg="#fff", bg="#00698f")
        self.add_tasks_button.pack(pady=10)

        self.operation_label = tk.Label(root, text="Select an operation:", font=("Times New Roman", 12), fg="#333", bg="#f0f0f0")
        self.operation_label.pack()
        self.operation_var = tk.StringVar()
        self.operation_combobox = ttk.Combobox(root, textvariable=self.operation_var, values=["1. Add", "2. Update", "3. Delete", "4. View", "5. Exit"], font=("Times New Roman", 12), state="readonly")
        self.operation_combobox.pack()

        self.task_entry_label = tk.Label(root, text="Enter task:", font=("Times New Roman", 12), fg="#333", bg="#f0f0f0")
        self.task_entry_label.pack()
        self.task_entry = tk.Entry(root, width=20, font=("Times New Roman", 12), fg="#333", bg="#fff")
        self.task_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit, font=("Times New Roman", 12), fg="#fff", bg="#00698f")
        self.submit_button.pack(pady=10)

        self.tasks_label = tk.Label(root, text="Today's tasks:", font=("Times New Roman", 12), fg="#333", bg="#f0f0f0")
        self.tasks_label.pack()
        self.tasks_text = tk.Text(root, height=10, width=40, font=("Times New Roman", 12), fg="#333", bg="#fff")
        self.tasks_text.pack(pady=10)

    def add_tasks(self):
        try:
            total_task = int(self.total_task_entry.get())
            for i in range(1, total_task + 1):
                task_name = self.task_entry.get()
                self.tasks.append(task_name)
                self.task_entry.delete(0, tk.END)  # Clear the entry field
            self.tasks_text.delete(1.0, tk.END)
            self.tasks_text.insert(tk.END, f"Today's tasks are:\n{self.tasks}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def submit(self):
        operation = self.operation_var.get()
        task_name = self.task_entry.get()
        if operation == "1. Add":
            self.tasks.append(task_name)
            self.tasks_text.delete(1.0, tk.END)
            self.tasks_text.insert(tk.END, f"Today's tasks are:\n{self.tasks}")
            messagebox.showinfo("Success", f"Task '{task_name}' has been successfully added.")
        elif operation == "2. Update":
            if task_name in self.tasks:
                new_task_name = self.task_entry.get()
                ind = self.tasks.index(task_name)
                self.tasks[ind] = new_task_name
                self.tasks_text.delete(1.0, tk.END)
                self.tasks_text.insert(tk.END, f"Today's tasks are:\n{self.tasks}")
                messagebox.showinfo("Success", f"Task '{task_name}' has been updated to '{new_task_name}'.")
            else:
                messagebox.showerror("Error", "Task not found.")
        elif operation == "3. Delete":
            if task_name in self.tasks:
                ind = self.tasks.index(task_name)
                del self.tasks[ind]
                self.tasks_text.delete(1.0, tk.END)
                self.tasks_text.insert(tk.END, f"Today's tasks are:\n{self.tasks}")
                messagebox.showinfo("Success", f"Task '{task_name}' has been deleted.")
            else:
                messagebox.showerror("Error", "Task not found.")
        elif operation == "4. View":
            self.tasks_text.delete(1.0, tk.END)
            self.tasks_text.insert(tk.END, f"Today's tasks are:\n{self.tasks}")
        elif operation == "5. Exit":
            self.root.destroy()

root = tk.Tk()
app = TaskManagementApp(root)
root.mainloop()