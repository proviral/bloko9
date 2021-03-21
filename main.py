import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from Board import Board

board = Board()

kb = Keyboard(usb_hid.devices)

while True:
    for key in board.keys:
        if key['btn'].value:
            kb.press(key['keyCode'])
            time.sleep(board.key_press_timeout)
            kb.release(key['keyCode'])
    time.sleep(board.sleep_time)