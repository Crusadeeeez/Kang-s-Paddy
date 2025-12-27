import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.rotary import RotaryEncoderModule
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.keys import KC, MediaKeys

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D11, board.D10, board.D9, board.D8, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

rotary = RotaryEncoderModule(
    pins=((board.D3, board.D2),),
    clockwise=(MediaKeys.volume_up,),
    counter_clockwise=(MediaKeys.volume_down,),
)
keyboard.modules.append(rotary)

keyboard.keymap = [
    [
        KC.MACRO(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL)),
        KC.MACRO(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL)),
        KC.MACRO("https://youtu.be/u4ecB57jFhI?si=CQD8pjg7-mSy_NqU", KC.ENTER),
        KC.ENTER,
        KC.ENTER, 
    ]
]

if __name__ == "__main__":
    keyboard.go()
