import os
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
from collections import Counter
import numpy as np
from PIL import Image  # Import PIL to load images

UPLOAD_FOLDER = './static/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None  # Initialize as None to handle the GET request case
    color_count_dict = {}  # Initialize the dictionary for storing colors

    if request.method == 'POST':
        if 'img' not in request.files:
            return 'No file part in the form!', 400

        file1 = request.files['img']
        if file1.filename == '':
            return 'No selected file!', 400

        # Sanitize the filename
        filename = secure_filename(file1.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file1.save(file_path)

        # Generate the URL for the uploaded image
        image_url = url_for('static', filename=f'upload/{filename}')

        # Open the image using PIL and convert it to a NumPy array
        image = Image.open(file_path)
        data = np.asarray(image)

        # Reshape the array to a list of pixels
        pixels = data.reshape(-1, data.shape[-1])  # Flatten to (num_pixels, 3) for RGB images

        # Ensure all pixel data is tuple-based and valid
        valid_pixels = [tuple(pixel) for pixel in pixels]  # Convert each pixel to a tuple

        # Count occurrences of each color
        pixel_counts = Counter(valid_pixels)

        # Get the 10 most common colors
        most_common_colors = pixel_counts.most_common(10)

        # Populate the dictionary with color counts
        for color, count in most_common_colors:
            clean_color = tuple(map(int, color))  # Convert each element to a Python int
            color_count_dict[clean_color] = count

        # Return the page with the image URL and color data
        return render_template('index.html', image_url=image_url, values=color_count_dict)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5010, debug=True)
