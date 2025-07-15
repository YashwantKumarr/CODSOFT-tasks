import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# ---------------------- Main Window ----------------------
root = tk.Tk()
root.title("✨ To-Do List")
root.geometry("500x550")
root.config(bg="#fefefe")
root.resizable(False, False)

# ---------------------- Custom Styles ----------------------
style = ttk.Style()
style.theme_use('clam')

# Colors & Fonts
primary_color = "#4F46E5"   # Indigo
accent_color = "#10B981"    # Emerald
danger_color = "#EF4444"    # Red
bg_color = "#F9FAFB"        # Light gray
font_family = "Segoe UI"

style.configure("TButton",
    font=(font_family, 12),
    padding=8,
    background=primary_color,
    foreground="white")
style.map("TButton", background=[('active', accent_color)])

style.configure("Title.TLabel", font=(font_family, 20, "bold"), foreground=primary_color, background=bg_color)
style.configure("TEntry", font=(font_family, 12))

# ---------------------- Task Data ----------------------
tasks = []

# ---------------------- Helper Functions ----------------------
def get_location():
    # You can make this dynamic using IP-based APIs, but here it's fixed.
    return "Indore"

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# ---------------------- Main Functions ----------------------
def add_task():
    task = task_entry.get().strip()
    if task:
        full_task = f"{task} 📍{get_location()} 🕒 {get_timestamp()}"
        tasks.append(full_task)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Field", "Please enter a task.")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        del tasks[selected]
        update_list()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        if "✔️" not in tasks[selected]:
            tasks[selected] += " ✔️"
            update_list()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to mark done.")

def update_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# ---------------------- GUI Layout ----------------------
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

title_label = ttk.Label(main_frame, text="📝 My To-Do List", style="Title.TLabel")
title_label.pack(pady=(0, 20))

task_entry = ttk.Entry(main_frame, width=40)
task_entry.pack(pady=(0, 15))

btn_frame = ttk.Frame(main_frame)
btn_frame.pack(pady=10)

add_btn = ttk.Button(btn_frame, text="➕ Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = ttk.Button(btn_frame, text="✅ Mark Done", command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

delete_btn = ttk.Button(btn_frame, text="❌ Delete Task", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# ---------------------- Listbox Section ----------------------
list_frame = ttk.Frame(main_frame)
list_frame.pack(pady=15, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)

task_listbox = tk.Listbox(
    list_frame,
    width=45,
    height=12,
    font=(font_family, 12),
    bg="white",
    bd=2,
    relief="groove",
    yscrollcommand=scrollbar.set,
    selectbackground="#E0F2FE",
    highlightcolor=primary_color
)

scrollbar.config(command=task_listbox.yview)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ---------------------- Footer ----------------------
footer = tk.Label(root, text="Made with ❤️ using Python + Tkinter", font=("Segoe UI", 10), bg="#fefefe", fg="#9CA3AF")
footer.pack(side=tk.BOTTOM, pady=10)

# ---------------------- Run the App ----------------------
root.mainloop()
