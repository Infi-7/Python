from time import sleep
from PIL import ImageGrab, ImageOps
import numpy as np
import pyautogui
from selenium import webdriver

# Define the region for obstacle detection
DINOSAUR_REGION = (355, 1156, 480, 1212)

# Launch the browser and game
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()
driver.get("https://elgoog.im/dinosaur-game/")
sleep(5)

def detect_obstacle(region):
    screen = ImageGrab.grab(bbox=region)
    gray_image = ImageOps.grayscale(screen)
    pixel_array = np.array(gray_image)

    # Check for dark pixels (potential obstacles)
    dark_pixels = pixel_array < 150
    if dark_pixels.sum() > 10:
        return True
    return False

def jump():
    pyautogui.press('space')

# Start the game automatically
pyautogui.click(x=400, y=400)  # Adjust coordinates to focus the browser
pyautogui.press('space')
sleep(1)

while True:
    if detect_obstacle(DINOSAUR_REGION):
        jump()
        sleep(0.1)
    sleep(0.01)
