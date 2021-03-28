import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from Board import Board

board = Board()
kb = Keyboard(usb_hid.devices)

macro_top_left = [ Keycode.CTRL, Keycode.KEYPAD_SEVEN ]
macro_top = [ Keycode.CTRL, Keycode.KEYPAD_EIGHT ]
macro_top_right = [ Keycode.CTRL, Keycode.KEYPAD_NINE ]
macro_left = [ Keycode.CTRL, Keycode.KEYPAD_FOUR ]
macro_center = [ Keycode.CTRL, Keycode.KEYPAD_FIVE ]
macro_right = [ Keycode.CTRL, Keycode.KEYPAD_SIX ]
macro_bottom = [ Keycode.CTRL, Keycode.KEYPAD_TWO ]

while True:
    if (board.bottom_left.value):
        keyboard.press(Keycode.SHIFT)
    if (board.bottom_right.value):
        keyboard.press(Keycode.ALT)

    if (board.top_left.value):
        keyboard.press(*macro_top_left)
    elif (board.top.value):
        keyboard.press(*macro_top)
    elif (board.top_right.value):
        keyboard.press(*macro_top_right)
    elif (board.left.value):
        keyboard.press(*macro_left)
    elif (board.center.value):
        keyboard.press(*macro_center)
    elif (board.right.value):
        keyboard.press(*macro_right)
    elif (board.bottom.value):
        keyboard.press(*macro_bottom)

    time.sleep(0.5)
    keyboard.release_all()

    time.sleep(0.5)