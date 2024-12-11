from pynput import mouse, keyboard
import time as t

# Global variable to keep track of the current scroll position
current_scroll_position = 0
# Variable to keep track of the number of down scrolls
down_scroll_count = 0
# Variable to keep track of whether the listener is active or not
listener_active = False
# Variable to store the mouse listener
mouse_listener = None

def on_scroll(x, y, dx, dy):
    global current_scroll_position, down_scroll_count
    # Update the current scroll position
    current_scroll_position += dy
    # Check if scrolling down
    if dy < 0:  # corrected comparison operator
        # Increment down scroll count
        down_scroll_count += 1
        # trigger crouch button 'c'
        keyboard.Controller().press(' ')
        t.sleep(0.004)
        keyboard.Controller().release(' ')
        t.sleep(0.004)
        keyboard.Controller().press('c')
        t.sleep(0.004)
        keyboard.Controller().release('c')
        keyboard.Controller().press(' ')
        t.sleep(0.004)
        keyboard.Controller().release(' ')
        t.sleep(0.004)
        keyboard.Controller().press('c')
        t.sleep(0.004)
        keyboard.Controller().release('c')
        # Check if down scroll count has reached 10
        if down_scroll_count == 6:  # corrected comparison operator
            # Deactivate the listener
            deactivate_listener()

def activate_listener():
    global listener_active, mouse_listener, down_scroll_count
    if not listener_active:
        # Start the mouse listener
        global mouse_listener
        mouse_listener = mouse.Listener(on_scroll=on_scroll)
        mouse_listener.start()
        print("superglide activated!")  # corrected print statement
        listener_active = True
        down_scroll_count = 0  # Reset down scroll count

def deactivate_listener():
    global listener_active, mouse_listener
    if listener_active:
        # Stop the mouse listener
        if mouse_listener:
            mouse_listener.stop()
        print("superglide deactivated!")  # corrected print statement
        listener_active = False

def on_key_press(key):
    global listener_active
    try:
        # Check if the pressed key is 'z'
        if key.char == 'z':
            if listener_active:
                deactivate_listener()
            else:
                activate_listener()
    except AttributeError:
        pass


print("press 'z' to activate")  # corrected print statement

# Set up the listener for key presses
keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()

# Keep the script running
keyboard_listener.join()
