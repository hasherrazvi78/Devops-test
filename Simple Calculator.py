import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        label_result.config(text=f"Result: {result:.2f}", fg="#4CAF50")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except ZeroDivisionError as zde:
        messagebox.showerror("Math Error", str(zde))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Stylish Calculator")
window.geometry("400x350")
window.configure(bg="#e0f7fa")

# Define a style for buttons
def style_button(button):
    button.config(
        font=('Arial', 12, 'bold'),
        bg='#00796b',
        fg='white',
        padx=20,
        pady=10,
        relief='raised',
        bd=4,
        highlightbackground='#004d40',
        highlightcolor='#004d40'
    )
    button.bind('<Enter>', lambda e: button.config(bg='#004d40'))
    button.bind('<Leave>', lambda e: button.config(bg='#00796b'))

# Create and place the widgets with styling
title_font = tkfont.Font(family='Arial', size=14, weight='bold')

tk.Label(window, text="Simple Calculator", bg="#e0f7fa", font=title_font, fg='#00796b').grid(row=0, column=0, columnspan=2, padx=20, pady=10)

tk.Label(window, text="Number 1:", bg="#e0f7fa", font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=20, pady=10, sticky='w')
entry_num1 = tk.Entry(window, font=('Arial', 12), bd=2, relief='solid')
entry_num1.grid(row=1, column=1, padx=20, pady=10)

tk.Label(window, text="Number 2:", bg="#e0f7fa", font=('Arial', 12, 'bold')).grid(row=2, column=0, padx=20, pady=10, sticky='w')
entry_num2 = tk.Entry(window, font=('Arial', 12), bd=2, relief='solid')
entry_num2.grid(row=2, column=1, padx=20, pady=10)

tk.Label(window, text="Operation:", bg="#e0f7fa", font=('Arial', 12, 'bold')).grid(row=3, column=0, padx=20, pady=10, sticky='w')
operation_var = tk.StringVar(value='+')
tk.OptionMenu(window, operation_var, '+', '-', '*', '/').grid(row=3, column=1, padx=20, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
style_button(calculate_button)
calculate_button.grid(row=4, column=0, columnspan=2, padx=20, pady=15)

label_result = tk.Label(window, text="Result:", bg="#e0f7fa", font=('Arial', 14, 'bold'))
label_result.grid(row=5, column=0, columnspan=2, padx=20, pady=15)

# Run the Tkinter event loop
window.mainloop()
