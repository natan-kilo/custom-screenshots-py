import configparser
import os

def get_config():
    cp = configparser.ConfigParser()
    if not os.path.exists("config.cfg"):
        create_default_config()
    cp.read("config.cfg")
    return cp

def create_default_config():
    cp = configparser.ConfigParser()
    cp["DEFAULT"] = {
        "hotkey_select_next_page":"ctrl + shift + 0",
        "hotkey_select_screen_start":"ctrl + shift + 9",
        "hotkey_select_screen_end":"ctrl + shift + 8",
        "hotkey_start_screenshots":"ctrl + shift + 7"
    }
    with open("config.cfg", "w") as file:
        cp.write(file)

