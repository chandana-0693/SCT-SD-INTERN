import tkinter as tk
import random

colors = ["#FFFACD", "#FFDAB9", "#E0FFFF", "#E6E6FA", "#F5FFFA", "#FFB6C1"]

class StickyNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Cute Sticky Notes")
        self.root.geometry("1000x650")
        self.root.configure(bg="#fefefe")

        # Heading
        heading = tk.Label(root, text="✨ Sticky Notes ✨", 
                           font=("Comic Sans MS", 22, "bold"), 
                           bg="#fefefe", fg="#FF69B4")
        heading.pack(pady=10)

        # Notes container
        self.notes_frame = tk.Frame(root, bg="#fefefe")
        self.notes_frame.pack(fill="both", expand=True, pady=10)

        # Bottom buttons
        btn_frame = tk.Frame(root, bg="#fefefe")
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="➕ Add Note", command=self.add_note,
                            font=("Comic Sans MS", 14, "bold"),
                            bg="#FFB6C1", fg="white", activebackground="#FF69B4",
                            activeforeground="white", relief="raised")
        add_btn.grid(row=0, column=0, padx=10)

        quit_btn = tk.Button(btn_frame, text="❌ Quit", command=root.quit,
                             font=("Comic Sans MS", 14, "bold"),
                             bg="#FF6961", fg="white", activebackground="#FF4500",
                             activeforeground="white", relief="raised")
        quit_btn.grid(row=0, column=1, padx=10)

        # Start with one note
        self.note_count = 0
        self.add_note()

    def add_note(self):
        color = random.choice(colors)

        # grid position (4 per row)
        row = self.note_count // 4
        col = self.note_count % 4

        note = tk.Frame(self.notes_frame, bg=color, bd=3, relief="ridge", padx=5, pady=5)
        note.grid(row=row, column=col, padx=10, pady=10)

        text = tk.Text(note, width=20, height=10, wrap="word", 
                       bg=color, font=("Comic Sans MS", 12))
        text.pack()

        # Buttons Frame inside note
        btns = tk.Frame(note, bg=color)
        btns.pack(fill="x", pady=3)

        # Edit button
        def toggle_edit():
            if text.cget("state") == "normal":
                text.config(state="disabled")
                edit_btn.config(text="✏️ Edit")
            else:
                text.config(state="normal")
                edit_btn.config(text="🔒 Lock")

        edit_btn = tk.Button(btns, text="✏️ Edit", command=toggle_edit, bd=0, 
                             font=("Arial", 10), bg=color)
        edit_btn.pack(side="left")

        # Pin button
        def pin_note():
            note.lift()  # bring note to front
            note.config(highlightbackground="red", highlightthickness=2)

        pin_btn = tk.Button(btns, text="📌 Pin", command=pin_note, bd=0, 
                            font=("Arial", 10), bg=color)
        pin_btn.pack(side="left", padx=5)

        # Delete button
        delete_btn = tk.Button(btns, text="❌", command=lambda: note.destroy(), 
                               bd=0, font=("Arial", 10), bg=color)
        delete_btn.pack(side="right")

        self.note_count += 1


# Run app
root = tk.Tk()
app = StickyNotesApp(root)
root.mainloop()
