from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog

PADDING = 30
WIN_WIDTH = 700
WIN_HEIGHT = 500

# Global variable to store the loaded image
loaded_image = None


def import_file():
    global loaded_image
    file_path = filedialog.askopenfilename(
        title="Select a file:",
        filetypes=[("PNG File", "*.PNG"), ("JPEG File", "*.JPEG"), ("All files", "*.*")]
    )
    if file_path:
        print("Image successfully selected")
        print(f"Image Path is: {file_path}")
        loaded_image = Image.open(file_path)
        loaded_image.thumbnail((WIN_WIDTH, WIN_HEIGHT))  # Resize to fit canvas

        # Convert for display in Tkinter
        img_tk = ImageTk.PhotoImage(loaded_image)

        # Store and display the image
        canvas.image = img_tk
        canvas.create_image(img_tk.width() / 2, img_tk.height() / 2, image=img_tk)
        print("Image displayed successfully")

        # Enable watermark button
        button_mark.config(state=NORMAL)
    else:
        print("No file selected.")


def add_watermark():
    global image_displayed
    global loaded_image
    if loaded_image is None:
        print("No image loaded.")
        return

    # Get watermark text and position
    watermark_text = text.get("1.0", END).strip()
    loc = clicked.get()

    temp_img = ImageTk.PhotoImage(loaded_image)

    positions={
        "Top Left":(10,10),
        "Top Right":(temp_img.width() - 150, 10),
        "Bottom Left":(10, temp_img.height() - 90),
        "Bottom Right": (temp_img.width() - 150, temp_img.height() - 90)
    }

    # Ensure a valid watermark text and position are provided
    if not watermark_text or loc not in positions:
        print("Invalid input for watermark text or position.")
        return

    print(f"Adding watermark: '{watermark_text}' at {positions[loc]}")

    # Add watermark
    draw = ImageDraw.Draw(loaded_image)
    font = ImageFont.truetype("fonts/Inktype.ttf", 20)  # Use a standard font; replace if unavailable
    position = positions[loc]
    draw.text(position, watermark_text, fill="white", font=font)

    # Update display with watermarked image
    img_tk = ImageTk.PhotoImage(loaded_image)
    image_displayed = img_tk
    canvas.image = img_tk
    canvas.create_image(img_tk.width() / 2, img_tk.height() / 2, image=img_tk)
    print("Watermark added successfully!")


# Initialize main window
window = Tk()
window.title('WaterMarker')
window.minsize(WIN_WIDTH // 2, WIN_HEIGHT // 2)
window.config(width=WIN_WIDTH, height=WIN_HEIGHT, padx=PADDING, pady=PADDING, bg='black')

# Canvas for displaying image
canvas = Canvas(window, bg='white', height=400, width=600)
canvas.grid(row=0, column=0)

# Frame for buttons
frame_buttons = Frame(window, width=350, height=100, bg='black')
frame_buttons.grid(row=1, column=0, sticky='w', pady=(30, 0))

# Button to import file
button_browse = Button(frame_buttons, text="Import File", command=import_file)
button_browse.grid(row=2, column=0, pady=(15, 15), sticky='nsew')
button_browse.config(bg='black', fg='white')

# Button to add watermark
button_mark = Button(frame_buttons, text="Add Watermark", state=DISABLED, command=add_watermark)
button_mark.grid(row=3, column=0, pady=(0, 15))
button_mark.config(bg='black', fg='white')

# Frame for watermark input and position
frame_status = Frame(window, width=350, height=100, bg='black')
frame_status.grid(row=1, column=0, sticky='nse', pady=(10, 10))

# Label and input for watermark text
l_mark = Label(frame_status, text="Watermark Text", fg='white', bg='black')
l_mark.grid(row=0, column=0, sticky='nsew')

text = Text(frame_status, width=40, height=1)
text.grid(row=2, column=0, pady=(15, 15))

# Label and dropdown for position
l_pos = Label(frame_status, text="Watermark Position", fg='white', bg='black')
l_pos.grid(row=3, column=0, sticky='nsew')

options = [
    "Top Left",
    "Top Right",
    "Bottom Left",
    "Bottom Right"
]

clicked = StringVar()
clicked.set(options[0])  # Default position
drop = OptionMenu(frame_status, clicked, *options)
drop.grid(row=4, column=0, pady=(15, 15))

window.mainloop()
