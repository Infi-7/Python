from time import sleep
from PIL import ImageGrab, ImageOps
import numpy as np

import pyautogui
from selenium import webdriver

DINOSAUR_REGION = (355, 1156, 480, 1212)

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)  # or whichever browser you're using
driver.maximize_window()
driver.get("https://elgoog.im/dinosaur-game/")

sleep(10)

# Get browser window size
window_size = driver.get_window_size()
width = window_size["width"]
height = window_size["height"]

# print(f"Browser resolution: {width}x{height}")


def detect_obstacle(region):
    # Capture the screen region
    screen = ImageGrab.grab(bbox=region)

    # Convert the image to grayscale
    gray_image = ImageOps.grayscale(screen)

    # Convert to numpy array for pixel analysis
    pixel_array = np.array(gray_image)

    # Check for dark pixels (potential obstacles)
    dark_pixels = pixel_array < 50  # Threshold for dark pixels
    if dark_pixels.any():  # Trigger if enough dark pixels are detected
        return True
    return False

def jump():
    pyautogui.press('space')

sleep(10)
jump()
sleep(2)
while True:
    #print(pyautogui.position())
    print(detect_obstacle(DINOSAUR_REGION))



