import tkinter as tk
from tkinter import messagebox, ttk

def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("⚠ Input Error", "Please enter a task!")
    else:
        task_list.insert("", "end", values=(task, "❌ Pending"))
        entry.delete(0, tk.END)

def delete_task():
    selected = task_list.selection()
    if not selected:
        messagebox.showwarning("⚠ Delete Error", "Please select a task to delete!")
    else:
        for item in selected:
            task_list.delete(item)

def mark_done():
    selected = task_list.selection()
    if not selected:
        messagebox.showwarning("⚠ Update Error", "Please select a task to mark as done!")
    else:
        for item in selected:
            task = task_list.item(item, "values")[0]
            task_list.item(item, values=(task, "✅ Completed"))

# Main Window
root = tk.Tk()
root.title("🌈 Stylish To-Do List")
root.geometry("600x500")
root.configure(bg="#1e1e2f")

# Title Banner
title_label = tk.Label(root, text="✨ My To-Do List ✨", 
                       font=("Comic Sans MS", 22, "bold"),
                       fg="#ffffff", bg="#1e1e2f")
title_label.pack(pady=15)

# Entry Frame
frame = tk.Frame(root, bg="#2e2e44", bd=3, relief="ridge")
frame.pack(pady=10, padx=10, fill="x")

entry = tk.Entry(frame, font=("Segoe UI", 14), width=25, bg="#fdfdfd", fg="#333")
entry.grid(row=0, column=0, padx=10, pady=10, sticky="we")

add_btn = tk.Button(frame, text="➕ Add Task", command=add_task,
                    bg="#6a5acd", fg="white", font=("Segoe UI", 12, "bold"),
                    relief="raised", width=12)
add_btn.grid(row=0, column=1, padx=10, pady=10)

frame.grid_columnconfigure(0, weight=1)  # entry expands only

# Task List
style = ttk.Style()
style.configure("Treeview",
                background="#f0f0f5",
                foreground="#000",
                rowheight=28,
                fieldbackground="#f0f0f5")
style.map("Treeview",
          background=[("selected", "#6a5acd")],
          foreground=[("selected", "#ffffff")])

columns = ("Task", "Status")
task_list = ttk.Treeview(root, columns=columns, show="headings", height=10)
task_list.heading("Task", text="📝 Task")
task_list.heading("Status", text="📌 Status")
task_list.column("Task", width=350)
task_list.column("Status", width=150)
task_list.pack(pady=15, padx=10, fill="both", expand=True)

# Button Toolbar (One Row, Fixed Width)
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=15)

done_btn = tk.Button(btn_frame, text="✅ Mark Done", command=mark_done,
                     bg="#32cd32", fg="white", font=("Segoe UI", 12, "bold"),
                     relief="raised", width=15)
done_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(btn_frame, text="🗑 Delete Task", command=delete_task,
                       bg="#ff4d4d", fg="white", font=("Segoe UI", 12, "bold"),
                       relief="raised", width=15)
delete_btn.grid(row=0, column=1, padx=10)

quit_btn = tk.Button(btn_frame, text="🚪 Quit", command=root.quit,
                     bg="#333", fg="white", font=("Segoe UI", 12, "bold"),
                     relief="raised", width=15)
quit_btn.grid(row=0, column=2, padx=10)

# Footer
footer = tk.Label(root, text="✨ Designed with ❤️ in Tkinter ✨", 
                  font=("Comic Sans MS", 10), fg="#ccc", bg="#1e1e2f")
footer.pack(side="bottom", pady=5)

root.mainloop()
