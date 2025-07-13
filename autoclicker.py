from pynput.keyboard import Controller
import time
import random

keyboard = Controller()

time.sleep(2)

while True:
    key_to_press = random.randint(0, 3)
    if key_to_press == 0:
        keyboard.press('a')
        time.sleep(2)
        keyboard.release('a')
    elif key_to_press == 1:
        keyboard.press('s')
        time.sleep(2)
        keyboard.release('s')
    elif key_to_press == 2:
        keyboard.press('w')
        time.sleep(2)
        keyboard.release('w')
    elif key_to_press == 3:
        keyboard.press('d')
        time.sleep(2)
        keyboard.release('d')

    time.sleep(2)