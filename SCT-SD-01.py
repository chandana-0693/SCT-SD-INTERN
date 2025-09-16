import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        scale = var.get()
        
        if scale == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result.set(f"{temp} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")
        elif scale == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result.set(f"{temp} °F = {celsius:.2f} °C = {kelvin:.2f} K")
        elif scale == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result.set(f"{temp} K = {celsius:.2f} °C = {fahrenheit:.2f} °F")
    except:
        messagebox.showerror("Error", "Please enter a valid number!")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("420x500")
root.config(bg="#E8F9FD")

# Load thermometer image (use your own "thermometer.jpg")
try:
    img = Image.open("thermometer.png")  # <-- Put an image named thermometer.png in same folder
    img = img.resize((120, 200))
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo, bg="#E8F9FD").pack(pady=10)
except:
    tk.Label(root, text="🌡️", font=("Arial", 50), bg="#E8F9FD").pack(pady=10)

# Heading
tk.Label(root, text="Temperature Converter", font=("Helvetica", 18, "bold"), bg="#E8F9FD", fg="#0077B6").pack(pady=5)

# Input box
tk.Label(root, text="Enter Temperature:", font=("Arial", 12), bg="#E8F9FD").pack()
entry_temp = tk.Entry(root, font=("Arial", 12), justify="center", bg="#F1FAEE")
entry_temp.pack(pady=5)

# Radio buttons
var = tk.StringVar(value="Celsius")
frame = tk.Frame(root, bg="#E8F9FD")
frame.pack(pady=5)
tk.Radiobutton(frame, text="Celsius", variable=var, value="Celsius", font=("Arial", 11), bg="#E8F9FD").grid(row=0, column=0, padx=10)
tk.Radiobutton(frame, text="Fahrenheit", variable=var, value="Fahrenheit", font=("Arial", 11), bg="#E8F9FD").grid(row=0, column=1, padx=10)
tk.Radiobutton(frame, text="Kelvin", variable=var, value="Kelvin", font=("Arial", 11), bg="#E8F9FD").grid(row=0, column=2, padx=10)

# Convert button
tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 13, "bold"), bg="#06D6A0", fg="white", width=12, relief="raised").pack(pady=10)

# Result label
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="#1D3557", bg="#E8F9FD", wraplength=350, justify="center").pack(pady=10)

# Quit button
tk.Button(root, text="Quit", command=root.destroy, font=("Arial", 11, "bold"), bg="#EF476F", fg="white", width=10).pack(pady=20)

root.mainloop()
