import pyautogui
import keyboard

print("clicker initialized")
run = False

while (True): 
        
    if run: pyautogui.click()
    
    if keyboard.is_pressed("ctrl+shift+g"):
        print("clicker starting..")
        run = True
    
    if keyboard.is_pressed("ctrl+shift+h"): 
        print("clicker stopping..")
        run = False

    if keyboard.is_pressed("ctrl+shift+j"): 
        print("clicker quitting..")
        quit()
