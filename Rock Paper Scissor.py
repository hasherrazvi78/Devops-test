import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "User"
    else:
        return "Computer"

def play_game(user_choice):
    global user_score, computer_score

    # Disable buttons to prevent multiple clicks during animation
    for button in [button_rock, button_paper, button_scissors]:
        button.config(state='disabled')
    
    computer_choice = get_computer_choice()
    label_computer_choice.config(text="Computer is choosing...")
    
    # Animate the computer choice
    window.after(1000, lambda: show_computer_choice(computer_choice, user_choice))

def show_computer_choice(computer_choice, user_choice):
    global user_score, computer_score

    label_computer_choice.config(text=f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)

    if result == "User":
        user_score += 1
        result_message = "You win!"
    elif result == "Computer":
        computer_score += 1
        result_message = "You lose!"
    else:
        result_message = "It's a tie!"

    # Update the result label with animation
    label_result.config(text="Result: " + result_message)
    fade_in_result()

    # Update the scores
    label_user_score.config(text=f"Your Score: {user_score}")
    label_computer_score.config(text=f"Computer Score: {computer_score}")

    # Re-enable buttons
    for button in [button_rock, button_paper, button_scissors]:
        button.config(state='normal')

def fade_in_result():
    current_color = "#f0f8ff"
    final_color = "#4CAF50"
    steps = 20
    step_delay = 50

    def step_fade(index):
        nonlocal current_color
        if index < steps:
            # Lighten the color by updating the result label's background
            new_color = blend_colors(current_color, final_color, index / steps)
            label_result.config(fg=new_color)
            window.after(step_delay, lambda: step_fade(index + 1))
    
    step_fade(0)

def blend_colors(color1, color2, factor):
    """Blend two colors together based on the factor"""
    r1, g1, b1 = [int(color1[i:i+2], 16) for i in (1, 3, 5)]
    r2, g2, b2 = [int(color2[i:i+2], 16) for i in (1, 3, 5)]
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return f"#{r:02x}{g:02x}{b:02x}"

def play_again():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_score.config(text=f"Your Score: {user_score}")
    label_computer_score.config(text=f"Computer Score: {computer_score}")
    label_computer_choice.config(text="Computer chose:")
    label_result.config(text="Choose Rock, Paper, or Scissors!")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
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

def animate_button_press(button):
    original_color = button.cget('bg')
    button.config(bg='#004d40')
    window.after(100, lambda: button.config(bg=original_color))

# Create and place the widgets with styling
title_font = ('Arial', 14, 'bold')

tk.Label(window, text="Rock-Paper-Scissors Game", bg="#e0f7fa", font=title_font, fg='#00796b').pack(pady=10)

frame_buttons = tk.Frame(window, bg="#e0f7fa")
frame_buttons.pack(pady=10)

button_rock = tk.Button(frame_buttons, text="Rock", command=lambda: [play_game('Rock'), animate_button_press(button_rock)])
style_button(button_rock)
button_rock.grid(row=0, column=0, padx=10)

button_paper = tk.Button(frame_buttons, text="Paper", command=lambda: [play_game('Paper'), animate_button_press(button_paper)])
style_button(button_paper)
button_paper.grid(row=0, column=1, padx=10)

button_scissors = tk.Button(frame_buttons, text="Scissors", command=lambda: [play_game('Scissors'), animate_button_press(button_scissors)])
style_button(button_scissors)
button_scissors.grid(row=0, column=2, padx=10)

label_computer_choice = tk.Label(window, text="Computer chose:", bg="#e0f7fa", font=('Arial', 12))
label_computer_choice.pack(pady=10)

label_result = tk.Label(window, text="Choose Rock, Paper, or Scissors!", bg="#e0f7fa", font=('Arial', 12, 'bold'))
label_result.pack(pady=10)

frame_scores = tk.Frame(window, bg="#e0f7fa")
frame_scores.pack(pady=10)

label_user_score = tk.Label(frame_scores, text=f"Your Score: {user_score}", bg="#e0f7fa", font=('Arial', 12))
label_user_score.grid(row=0, column=0, padx=20)

label_computer_score = tk.Label(frame_scores, text=f"Computer Score: {computer_score}", bg="#e0f7fa", font=('Arial', 12))
label_computer_score.grid(row=0, column=1, padx=20)

button_play_again = tk.Button(window, text="Play Again", command=play_again)
style_button(button_play_again)
button_play_again.pack(pady=15)

# Run the Tkinter event loop
window.mainloop()
