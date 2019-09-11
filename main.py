import keyboard
import win32gui
import win32api
import win32con
from config import get_config
import classes
import os

# region mouse

def get_mouse_pos():
    return win32gui.GetCursorPos()

def set_mouse_pos(pos):
    win32api.SetCursorPos(pos)

def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def click_pos(pos):
    set_mouse_pos(pos)
    click(pos[0], pos[1])


# endregion

# region pre_initialization

config = get_config()
hotkey_set_next_page = config["DEFAULT"]["hotkey_select_next_page"]
hotkey_set_screen_start = config["DEFAULT"]["hotkey_select_screen_start"]
hotkey_set_screen_end = config["DEFAULT"]["hotkey_select_screen_end"]
hotkey_start = config["DEFAULT"]["hotkey_start_screenshots"]

screen_manager = classes.custom(click_pos)
screen_manager.set_screenshot_folder("screenshots")
screen_manager.create_screenshot_folder()
screen_manager.delay = 1

amount = 0

# endregion

# region functions

def set_next_page():
    pos = get_mouse_pos()
    screen_manager.set_next_page_pos(pos)

def set_screen_start():
    pos = get_mouse_pos()
    screen_manager.set_screenshot_startpos(pos)

def set_screen_end():
    pos = get_mouse_pos()
    screen_manager.set_screenshot_endpos(pos)

def start():
    for i in range(amount):
        screen_manager.create_screenshot(i)


# endregion



# region keyboard

keyboard.add_hotkey(hotkey_set_next_page, set_next_page)
keyboard.add_hotkey(hotkey_set_screen_start, set_screen_start)
keyboard.add_hotkey(hotkey_set_screen_end, set_screen_end)
keyboard.add_hotkey(hotkey_start, start)

# endregion


amount = int(input("Please input the amount of screenshots - "))
os.system("pause")
print("Press '{}' to start.".format(hotkey_start))