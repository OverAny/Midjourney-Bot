from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)
print("run")

#example
list = ["/imagine girl", "/imagine boy"]


#5 seconds to hover over discord input

for a in list:
    for char in a:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)
    keyboard.press(Key.enter)
    time.sleep(0.22)

