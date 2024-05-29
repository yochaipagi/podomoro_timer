from tkinter import *
import math
from tkinter import simpledialog

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✓"
timer = None
counter = 0

# ---------------------------- FUNCTIONS ------------------------------- #
def reset_timer():
    global counter, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_labels.config(text="")
    counter = 0

def start_timer():
    global counter
    counter += 1
    if counter % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif counter % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    if counter == reps:
        reset_timer()

def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(counter / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_labels.config(text=marks)

def get_user_inputs():
    global reps, work_sec, short_break_sec, long_break_sec
    reps = simpledialog.askinteger("Input", "Enter number of work sessions:") * 2  # Each work session is followed by a break
    work_sec = simpledialog.askinteger("Input", "Enter work time in minutes:") * 60
    short_break_sec = simpledialog.askinteger("Input", "Enter short break time in minutes:") * 60
    long_break_sec = simpledialog.askinteger("Input", "Enter long break time in minutes:") * 60

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_labels = Label(fg=GREEN, bg=YELLOW, text="")
check_labels.grid(column=1, row=3)

# Get user inputs for the number of work sessions and durations
get_user_inputs()

window.mainloop()
