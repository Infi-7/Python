from tkinter import *

timer = None
text_input = ''

def start_count(event):
    global timer, text_input

    if timer is not None:
        window.after_cancel(timer)
    if event.keysym == "BackSpace":
        text_input = text_input[:-1]
    elif event.char:
        text_input += event.char
    timer = window.after(5000, reset_app)

def reset_app():
    global timer, text_input
    area.delete('1.0', 'end')
    text_input = ""
    timer = None

window = Tk()
window.title('Disappearing Text')
window.config(bg='black', width=400, height=300, padx=20, pady=10)
window.resizable(False, False)

warning = Label(
    window,
    text='The text will disappear in 5 seconds after typing is stopped.',
    bg='black',
    fg='white',
)

area = Text(window, width=50, height=10)

reset_button = Button(window, text='Reset', bg='black', fg='white', command=reset_app)

area.bind('<KeyPress>', start_count)

warning.grid(row=0, column=0, columnspan=2, pady=(0, 10))
area.grid(row=1, column=0, columnspan=2, pady=(0, 10))
reset_button.grid(row=2, column=0, columnspan=2)

window.mainloop()
