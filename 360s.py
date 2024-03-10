print("lets take a screenshot")
from inputs import get_gamepad
import keyboard

# Define your Xbox controller button mappings
BACK_BUTTON = 'BTN_GAMEPAD'  # Replace with the correct button ID for "Back"
START_BUTTON = 'BTN_GAMEPAD'  # Replace with the correct button ID for "Start"

# Define the key combination to trigger the screenshot (Alt + F1)
SCREENSHOT_SHORTCUT = 'alt+f1'#win+print_sscreen +f1

# Initialize variables
back_pressed = start_pressed = False
t= 1
while True:
    try:
      events = get_gamepad()
    except :
        print("controller not found ")
        break
    for event in events:    
        if event.ev_type == 'Key' and event.state == 1:
            if event.code == BACK_BUTTON:
                back_pressed = True
            elif event.code == START_BUTTON:
                start_pressed = True
            else:
                back_pressed = start_pressed = False

    if back_pressed and start_pressed:
        keyboard.press_and_release(SCREENSHOT_SHORTCUT)
        print(t," Screenshot taken")
        t+=1
        back_pressed = start_pressed = False
print("bye next time")