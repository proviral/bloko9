import board
import digitalio
from adafruit_hid.keycode import Keycode

class Board:
    __pin1 = board.GP28
    __pin2 = board.GP2
    __pin3 = board.GP5
    __pin4 = board.GP27
    __pin5 = board.GP11
    __pin6 = board.GP7
    __pin7 = board.GP19
    __pin8 = board.GP17
    __pin9 = board.GP14

    top_left = digitalio.DigitalInOut(__pin1)
    top_left.direction = digitalio.Direction.INPUT
    top_left.pull = digitalio.Pull.DOWN

    top = digitalio.DigitalInOut(__pin2)
    top.direction = digitalio.Direction.INPUT
    top.pull = digitalio.Pull.DOWN

    top_right = digitalio.DigitalInOut(__pin3)
    top_right.direction = digitalio.Direction.INPUT
    top_right.pull = digitalio.Pull.DOWN

    left = digitalio.DigitalInOut(__pin4)
    left.direction = digitalio.Direction.INPUT
    left.pull = digitalio.Pull.DOWN

    center = digitalio.DigitalInOut(__pin5)
    center.direction = digitalio.Direction.INPUT
    center.pull = digitalio.Pull.DOWN

    right = digitalio.DigitalInOut(__pin6)
    right.direction = digitalio.Direction.INPUT
    right.pull = digitalio.Pull.DOWN

    bottom_left = digitalio.DigitalInOut(__pin7)
    bottom_left.direction = digitalio.Direction.INPUT
    bottom_left.pull = digitalio.Pull.DOWN

    bottom = digitalio.DigitalInOut(__pin8)
    bottom.direction = digitalio.Direction.INPUT
    bottom.pull = digitalio.Pull.DOWN

    bottom_right = digitalio.DigitalInOut(__pin9)
    bottom_right.direction = digitalio.Direction.INPUT
    bottom_right.pull = digitalio.Pull.DOWN
