from PIL import ImageGrab
import os
import time

class custom:
    def __init__(self, click_func):
        self.next_page_pos = None
        self.screenshot_start_pos = None
        self.screenshot_end_pos = None
        self.screenshot_folder = None
        self.screenshot_folder_exists = False
        self.click = click_func
        self.delay = 0
    def set_screenshot_startpos(self, pos):
        self.screenshot_start_pos = pos
    def set_screenshot_endpos(self, pos):
        self.screenshot_end_pos = pos
    def set_next_page_pos(self, pos):
        self.next_page_pos = pos
    def set_screenshot_folder(self, name):
        self.screenshot_folder = name
    def create_screenshot_folder(self):
        if self.screenshot_folder is not None:
            if not os.path.exists(self.screenshot_folder):
                os.mkdir(os.path.join(os.getcwd(), self.screenshot_folder))
                self.screenshot_folder_exists = True
            else:
                self.screenshot_folder_exists = True
    def create_screenshot(self, page_index):
        if self.screenshot_folder_exists:
            if self.next_page_pos is not None:
                if self.screenshot_start_pos is not None:
                    if self.screenshot_end_pos is not None:
                        x = self.screenshot_start_pos[0]
                        y = self.screenshot_start_pos[1]
                        x_end = self.screenshot_end_pos[0]
                        y_end = self.screenshot_end_pos[1]
                        img = ImageGrab.grab((x, y, x_end, y_end))
                        img.save(os.path.join(os.getcwd(), self.screenshot_folder, "img-{}.png".format(page_index)))
                        self.click(self.next_page_pos)
                        time.sleep(self.delay)
                        return True

        raise Exception("Not all positions are defined!")