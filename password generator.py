import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, include_letters, include_digits, include_symbols, exclude_chars):
    """
    Generate a random password based on user preferences and exclusions.
    """
    # Ensure minimum length requirement
    if length < 8:
        messagebox.showerror("Invalid Length", "Password length should be at least 8 characters.")
        return ""
    
    # Create a string of possible characters based on the user's choices
    chars = ""
    if include_letters:
        chars += string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    # Remove excluded characters
    chars = ''.join(c for c in chars if c not in exclude_chars)

    # Check if at least one character type was selected
    if not chars:
        messagebox.showerror("No Characters Selected", "Please select at least one character type and ensure exclusions do not remove all possible characters.")
        return ""
    
    # Generate the password
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Ensure password complexity
        if (include_letters and not any(c.isalpha() for c in password)) or \
           (include_digits and not any(c.isdigit() for c in password)) or \
           (include_symbols and not any(c in string.punctuation for c in password)):
            continue  # Regenerate if not meeting complexity
        
        break  # Password meets all criteria, exit loop
    
    return password

def on_generate_password():
    """
    Callback function for the Generate Password button.
    """
    try:
        length = int(length_entry.get())
        include_letters = letters_var.get()
        include_digits = digits_var.get()
        include_symbols = symbols_var.get()
        exclude_chars = exclude_entry.get()
        password = generate_password(length, include_letters, include_digits, include_symbols, exclude_chars)
        if password:
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

def copy_to_clipboard():
    """
    Copy the generated password to the clipboard.
    """
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showerror("No Password", "No password to copy. Please generate a password first.")

# Initialize main window
window = tk.Tk()
window.title("Advanced Password Generator")

# Password length input
tk.Label(window, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Include letters checkbox
letters_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2)

# Include digits checkbox
digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2)

# Include symbols checkbox
symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2)

# Exclude characters input
tk.Label(window, text="Exclude Characters:").grid(row=4, column=0, padx=10, pady=5)
exclude_entry = tk.Entry(window)
exclude_entry.grid(row=4, column=1, padx=10, pady=5)

# Generate password button
tk.Button(window, text="Generate Password", command=on_generate_password).grid(row=5, column=0, columnspan=2, pady=10)

# Display generated password
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Copy to clipboard button
tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
window.mainloop()


