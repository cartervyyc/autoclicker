from pynput.keyboard import Controller
import time
import random

keyboard = Controller()

time.sleep(2)

while True:
    key_to_press = random.randint(0, 3)
    if key_to_press == 0:
        keyboard.press('a')
        keyboard.release('a')
    elif key_to_press == 1:
        keyboard.press('s')
        keyboard.release('s')
    elif key_to_press == 2:
        keyboard.press('w')
        keyboard.release('w')
    elif key_to_press == 3:
        keyboard.press('d')
        keyboard.release('d')

    time.sleep(2)