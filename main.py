from tkinter import *
import math
# FIX THE CHECK MARK

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'{0}:{0:02d}')
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    original_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(original_time)
        label.config(text="Timer", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec:02d}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image) #x, y, image
timer_text = canvas.create_text(100, 130, text="00.00", fill="White", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button2 = Button(text="Reset", highlightthickness=0, command=reset)
checkmark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
button1.grid(column=0, row=4)
button2.grid(column=2, row=4)
checkmark_label.grid(column=1, row=5)



window.mainloop()