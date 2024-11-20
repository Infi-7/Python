from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

PADDING = 30
WIDTH = 700
HEIGHT = 400

pos = {
    "Top Left":['n','e']
}

def import_file():
    file_path = filedialog.askopenfilename(title="Select a file:",filetypes=[("PNG File","*.PNG"),("JPEG File","*.JPEG"), ("All files", "*.*")])
    if file_path:
        print("Images successfully selected")
        print(f"Image Path is : {file_path}")
        img = Image.open(file_path)
        img.thumbnail((WIDTH, HEIGHT))
        img = ImageTk.PhotoImage(img)

        canvas.image = img
        canvas.create_image(img.width()/2, img.height()/2, image=img)
        print("Export Success")

        button_mark.config(state=NORMAL)

    else:
        import_file()

def get_data():
    watermark_text = text.get(1.0, END)
    loc = clicked.get()
    print(watermark_text)
    print(pos.get(loc))

    watermark = Label(canvas)
    watermark.grid(row=0, column=0)

window = Tk()

window.title('WaterMarker')
window.minsize(400,250)
window.config(width=700 , height=500, padx=PADDING, pady=PADDING, bg='black')

canvas = Canvas(window, bg='white', height=400, width=600)
canvas.grid(row=0, column=0)

frame_buttons = Frame(window, width=350, height=100, bg='black')
frame_buttons.grid(row=1, column=0, sticky='w', pady=(30,0))

button_browse = Button(frame_buttons,text="Import File", command=import_file)
button_browse.grid(row=2, column=0, pady=(15, 15), sticky='w'+'e'+'s'+'n')
button_browse.config(bg='black', fg='white')

button_mark = Button(frame_buttons,text="Add Water Mark", state=DISABLED , command=get_data)
button_mark.grid(row=3, column=0, pady=(0, 15))
button_mark.config(bg='black', fg='white')

frame_status = Frame(window, width=350, height=100, bg='black')
frame_status.grid(row=1, column=0, sticky='n'+'s'+'e', pady=(10,10))

l_mark = Label(frame_status, text = "Watermark Text", fg='white', bg='black')
l_mark.grid(row=0, column=0, sticky='w'+'e'+'s'+'n')

text = Text(frame_status, width=40, height=1)
text.grid(row=2, column=0, pady=(15, 15))

l_pos = Label(frame_status, text = "Watermark Position", fg='white', bg='black')
l_pos.grid(sticky='w'+'e'+'s'+'n')

options = [
    "Top Left",
    "Top Right",
    "Bottom Left",
    "Bottom Right"
]



clicked = StringVar()
drop = OptionMenu( frame_status , clicked , *options )
drop.grid(row=4, column=0, pady=(15, 15))

window.mainloop()