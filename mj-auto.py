from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("run")

import csv

def add_to_list(filename):
    result = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        z = 0
        first = True
        for row in reader:
            z += 1
            if first:
                first = False
            else: 
                result.append("/imagine " + row[1])

    return result

list_of_strings = add_to_list("prompts/final.csv")
print(list_of_strings)

#  starfish, turkey


#5 seconds to hover over discord input
print("about to type")
time.sleep(5)

time.sleep(7200)

index = 0
for a in list_of_strings:
    print("here")
    for char in a:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    print("here1")

    if index % 10 == 9:
        print("WAITING: " + str(index))
        time.sleep(300)
    index +=1
    

