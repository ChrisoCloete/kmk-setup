# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

# Using drive names (REDOXL, REDOXR) to recognize sides; use split_side arg if you're not doing it
split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
#split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

oneshot = OneShot()
keyboard.modules.append(oneshot)
keyboard.extensions.append(MediaKeys())
holdtap = HoldTap()
# optional: set a custom tap timeout in ms
# holdtap.tap_time = 300
keyboard.modules.append(holdtap)

keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.col_pins = (board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Cleaner key names  
_______ = KC.TRNS
XXXXXXX = KC.NO
OS_LCTL = KC.OS(KC.LCTL, tap_time=None)
OS_LSFT = KC.OS(KC.LSFT, tap_time=None)
EGUI  = RGUI = KC.HT(KC.ENTER, KC.RGUI)

#FnKey = KC.MO(1) 

keyboard.keymap = [
    # Base Layer
    [
        # COL GPL3      COL GPL4    COL GPL5    COL GPL6    COL GPL7    COL GPL8    <>  COL GPR8        COL GPR7    COL GPR6    COL GPR5    COL GPR4    COL GPR3

        KC.ESCAPE,       KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,          KC.Y,           KC.U,       KC.I,       KC.O,       KC.P,       KC.MINUS,\

        KC.TAB,          KC.A,       KC.S,       KC.D,       KC.F,       KC.G,              KC.H,        KC.J,       KC.K,       KC.L,      KC.SCOLON,   KC.QUOTE,\

        OS_LSFT,       KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,              KC.N,       KC.M,       KC.COMMA,    KC.DOT,    KC.SLASH,     KC.BSLASH,\

        OS_LCTL,       KC.LALT,     KC.LGUI,  KC.MO(1),    KC.SPACE,   KC.MO(2),          EGUI,       KC.BSPACE,  KC.FD(1),   KC.FD(2),    KC.RGUI,   KC.GRV,\

     ],

    # M1 Layer     
    [
        # COL GPL3      COL GPL4    COL GPL5    COL GPL6    COL GPL7    COL GPL8    <>  COL GPR8        COL GPR7    COL GPR6    COL GPR5    COL GPR4    COL GPR3

        KC.GRV,        KC.EXML,    KC.AT,      KC.HASH,    KC.DOLLAR,  KC.PERCENT,       KC.CIRC,        KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.EQUAL, \

        _______,        _______,    _______,    _______,   KC.RGUI(KC.B),KC.LBRACKET,     KC.LCBR,       KC.LEFT,   KC.UP,      KC.RIGHT,      _______,   _______, \

        OS_LSFT,        _______,    _______,    _______,    KC.HOME,   KC.RBRACKET,      KC.RCBR,        KC.END,    KC.DOWN,    _______,    _______,    _______, \

        _______,        _______,    _______,    KC.FD(0),    KC.SPACE,    _______,        EGUI,        KC.BSPACE,    KC.FD(2),    _______,    _______,    _______, \

    
     ],

    # M2 Layer        
    
     [
        # COL GPL3      COL GPL4    COL GPL5    COL GPL6    COL GPL7    COL GPL8        <>  COL GPR8        COL GPR7    COL GPR6    COL GPR5    COL GPR4        COL GPR3
        
        _______,      _______,    _______,      _______,    _______,    _______,              KC.MINUS,      KC.N7,      KC.N8,       KC.N9,      KC.BSPACE,      _______, \

        _______,        _______,   _______,KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,KC.PLUS,         KC.EQUAL,      KC.N4,      KC.N5,       KC.N6,      _______,     _______, \

        _______,        _______,    _______,KC.BRIGHTNESS_DOWN,KC.BRIGHTNESS_UP,KC.DOT,      KC.N0,        KC.N1,      KC.N2,       KC.N3,      _______,       _______, \

        _______,        _______,    _______,    KC.FD(0),    KC.SPACE,    _______,              EGUI,        KC.BSPACE,   KC.FD(1),     _______,    _______,     _______, \

    ],
]






if __name__ == '__main__':
    keyboard.go()
 
