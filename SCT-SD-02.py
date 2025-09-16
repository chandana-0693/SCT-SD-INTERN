import tkinter as tk
import random
from PIL import Image, ImageTk

def check_guess():
    try:
        guess = int(entry_guess.get())
        if guess == number:
            result.set("🎉 Correct! You guessed it!")
        elif guess < number:
            result.set("⬇️ Too Low! Try again.")
        else:
            result.set("⬆️ Too High! Try again.")
    except:
        result.set("❌ Enter a valid number!")

def reset_game():
    global number
    number = random.randint(1, 100)
    result.set("🔄 Game Reset! Guess a number between 1-100")
    entry_guess.delete(0, tk.END)

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🎲 Guess the Number Game")
root.geometry("420x500")
root.config(bg="#FFF8E7")

# Load game image (use your own "dice.png" or "question.png")
try:
    img = Image.open("dice.png")  # <-- put dice.png or question.png in same folder
    img = img.resize((120, 120))
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo, bg="#FFF8E7").pack(pady=10)
except:
    tk.Label(root, text="❓", font=("Arial", 60), bg="#FFF8E7").pack(pady=10)

# Heading
tk.Label(root, text="Guess the Number (1–100)", font=("Helvetica", 18, "bold"), bg="#FFF8E7", fg="#D00000").pack(pady=5)

# Input
tk.Label(root, text="Enter your guess:", font=("Arial", 12), bg="#FFF8E7").pack()
entry_guess = tk.Entry(root, font=("Arial", 12), justify="center", bg="#F1FAEE")
entry_guess.pack(pady=5)

# Buttons
tk.Button(root, text="Check Guess", command=check_guess, font=("Arial", 13, "bold"), bg="#06D6A0", fg="white", width=12).pack(pady=10)
tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 11, "bold"), bg="#118AB2", fg="white", width=12).pack()

# Result label
result = tk.StringVar(value="🎯 Start Guessing a number!")
tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="#1D3557", bg="#FFF8E7", wraplength=350, justify="center").pack(pady=20)

# Quit button
tk.Button(root, text="Quit", command=root.destroy, font=("Arial", 11, "bold"), bg="#EF476F", fg="white", width=10).pack(pady=20)

# Start with a random number
number = random.randint(1, 100)

root.mainloop()
