import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        try:
            password_length = int(entry_length.get())
            if password_length <= 0:
                raise ValueError("Length must be a positive integer.")
            
            password = generate_password(password_length)
            result_var.set(password)
        
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    # Create main window
    root = tk.Tk()
    root.title("Password Generator")

    # Frame for input and button
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    # Label and Entry for password length
    tk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
    entry_length = tk.Entry(frame, width=20)
    entry_length.grid(row=0, column=1, padx=5, pady=5)

    # Button to generate password
    generate_button = tk.Button(frame, text="Generate Password", command=generate)
    generate_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Label and Entry to display generated password
    tk.Label(frame, text="Generated Password:").grid(row=2, column=0, padx=5, pady=5)
    result_var = tk.StringVar()
    result_entry = tk.Entry(frame, textvariable=result_var, width=30, state='readonly')
    result_entry.grid(row=2, column=1, padx=5, pady=5)

    # Run the application
    root.mainloop()

# Run the GUI
generate_password_gui()
