from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

PADDING = 30
WIDTH = 700
HEIGHT = 400

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

    else:
        import_file()


window = Tk()
frame_buttons = Frame(window, width=350, height=100, bg='black')
frame_buttons.grid(row=1, column=0, sticky='w', pady=(30,0))


window.title('WaterMarker')
window.minsize(400,250)
window.config(width=700 , height=500, padx=PADDING, pady=PADDING, bg='black')

canvas = Canvas(window, bg='white', height=400, width=600)
canvas.grid(row=0, column=0)

button_browse = Button(frame_buttons,text="Import File", command=import_file)
button_browse.grid(row=2, column=0, pady=(15, 15), sticky='w'+'e'+'s'+'n')
button_browse.config(bg='black', fg='white')

button_mark = Button(frame_buttons,text="Add Water Mark")
button_mark.grid(row=3, column=0, pady=(0, 15))
button_mark.config(bg='black', fg='white')


window.mainloop()