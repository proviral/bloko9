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

    __btn1 = digitalio.DigitalInOut(__pin1)
    __btn1.direction = digitalio.Direction.INPUT
    __btn1.pull = digitalio.Pull.DOWN

    __btn2 = digitalio.DigitalInOut(__pin2)
    __btn2.direction = digitalio.Direction.INPUT
    __btn2.pull = digitalio.Pull.DOWN

    __btn3 = digitalio.DigitalInOut(__pin3)
    __btn3.direction = digitalio.Direction.INPUT
    __btn3.pull = digitalio.Pull.DOWN

    __btn4 = digitalio.DigitalInOut(__pin4)
    __btn4.direction = digitalio.Direction.INPUT
    __btn4.pull = digitalio.Pull.DOWN

    __btn5 = digitalio.DigitalInOut(__pin5)
    __btn5.direction = digitalio.Direction.INPUT
    __btn5.pull = digitalio.Pull.DOWN

    __btn6 = digitalio.DigitalInOut(__pin6)
    __btn6.direction = digitalio.Direction.INPUT
    __btn6.pull = digitalio.Pull.DOWN

    __btn7 = digitalio.DigitalInOut(__pin7)
    __btn7.direction = digitalio.Direction.INPUT
    __btn7.pull = digitalio.Pull.DOWN

    __btn8 = digitalio.DigitalInOut(__pin8)
    __btn8.direction = digitalio.Direction.INPUT
    __btn8.pull = digitalio.Pull.DOWN

    __btn9 = digitalio.DigitalInOut(__pin9)
    __btn9.direction = digitalio.Direction.INPUT
    __btn9.pull = digitalio.Pull.DOWN

    sleep_time = 0.05
    key_press_timeout = 0.07

    keys = [
        { "keyCode": Keycode.ONE, "btn": __btn1 },
        { "keyCode": Keycode.TWO, "btn": __btn2 },
        { "keyCode": Keycode.THREE, "btn": __btn3 },
        { "keyCode": Keycode.FOUR, "btn": __btn4 },
        { "keyCode": Keycode.FIVE, "btn": __btn5 },
        { "keyCode": Keycode.SIX, "btn": __btn6 },
        { "keyCode": Keycode.SEVEN, "btn": __btn7 },
        { "keyCode": Keycode.EIGHT, "btn": __btn8 },
        { "keyCode": Keycode.NINE, "btn": __btn9 }
    ]