from tkinter import *

WIDTH = 900
WIDTH_FRAME = (WIDTH - 20) /2
HEIGHT = 600
text = "Hello World!"

window = Tk()
window.title('Typing Speed Test')
window.config(width=WIDTH, height=HEIGHT, bg='black')
window.resizable(0,0)

# Frame to display Time Remaining
timer_frame = Frame(window, width=WIDTH_FRAME, height=HEIGHT/2, bg='white', border=1)
timer_frame.propagate(False)
timer_frame.place(x=10, y=10, relx=0.01, rely=0.01)

# Frame to display Accuracy
accuracy_frame = Frame(window, width=WIDTH_FRAME, height=HEIGHT/2, bg='yellow')
accuracy_frame.propagate(False)
accuracy_frame.place(x=430, y=10, relx=0.01, rely=0.01)

# Frame to display text input
main_frame = Frame(window, width=WIDTH-40, height=260, bg="cyan")
main_frame.propagate(False)
main_frame.place(x=10, y=320, relx=0.01, rely=0.01)
'''
timer_frame.config(borderwidth=1)
accuracy_frame.config(borderwidth=1)
'''
# Timer Label
timer_label = Label(timer_frame, text="Time Remaining", bg="black", fg="white", height=3)
timer_label.place(x=(WIDTH_FRAME/2)-70, y=30 ,relx=0.01, rely=0.01)

# Accuracy Label
accuracy_label = Label(accuracy_frame, text="Accuracy", bg="black", fg="white", height=3)
accuracy_label.place(x=(WIDTH_FRAME/2)-20, y=30, relx=0.01, rely=0.01)

# Text to be typed
text_label = Label(main_frame,text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
text_label.config(wraplength=WIDTH - 80, fg='black')
text_label.place(x=10, y=20, relx=0.01, rely=0.01)

text_input = Text(main_frame, height=6)
text_input.place(x=10, y=130, relx=0.01, rely=0.01)

window.mainloop()