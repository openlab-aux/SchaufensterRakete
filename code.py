import time
import board
import digitalio


import usb_hid
from adafruit_hid.keyboard import Keyboard
# from keyboard_layout_win_de import KeyboardLayout
# Brauchen wir nicht, wir senden nur die direkten Keys, ohne Text.
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

debug = False # wenn True, dann werden über Serial Debug-Meldungen ausgegeben

sleep_time = 0.01 # Zeit, die jeweils nach einem erkannten Tastendruck gewartet wird, um Prellen zu vermeiden
timer_sec = time.monotonic() # Time-Monotonic wird für den Timeout des Spiels verwendet


# Zuweisung der einzelnen Taster auf die Pins.
btn_1_pin      = board.GP15
btn_1_state    = False

btn_2_pin    = board.GP17
btn_2_state  = False

btn_3_pin    = board.GP14
btn_3_state  = False

btn_4_pin   = board.GP16
btn_4_state = False

btn_5_pin   = board.GP18
btn_5_state = False

# Pins werden auf Pull-Up und Input gestellt. 
btn_1_pin = digitalio.DigitalInOut(btn_1_pin)
btn_1_pin.direction = digitalio.Direction.INPUT
btn_1_pin.pull = digitalio.Pull.UP

btn_2_pin = digitalio.DigitalInOut(btn_2_pin)
btn_2_pin.direction = digitalio.Direction.INPUT
btn_2_pin.pull = digitalio.Pull.UP

btn_3_pin = digitalio.DigitalInOut(btn_3_pin)
btn_3_pin.direction = digitalio.Direction.INPUT
btn_3_pin.pull = digitalio.Pull.UP

btn_4_pin = digitalio.DigitalInOut(btn_4_pin)
btn_4_pin.direction = digitalio.Direction.INPUT
btn_4_pin.pull = digitalio.Pull.UP

btn_5_pin = digitalio.DigitalInOut(btn_5_pin)
btn_5_pin.direction = digitalio.Direction.INPUT
btn_5_pin.pull = digitalio.Pull.UP


# Wenn länger als 90 Sekunden keine Taste mehr gedrückt wurde, muss 2 mal Enter gedrückt werden um das Spiel neu zu starten.
def timeout():
    global timer_sec
    if debug:
        print(timer_sec)
        print(time.monotonic() - timer_sec)
    if (time.monotonic() - timer_sec) > 90:
        keyboard.release_all()
        keyboard.press(Keycode.ENTER) # Vorher mit keyboard.send gab es Probleme, dass der Rechner nur 1x Enter erkannt hatte.
        time.sleep(0.05)
        keyboard.release_all()
        if debug:
            print('enter 1')
            print(time.monotonic())
        time.sleep(1)
        keyboard.press(Keycode.ENTER)
        time.sleep(0.05)
        keyboard.release_all()
        if debug:
            print('enter 2')
            print(time.monotonic())
        time.sleep(1)
        if debug:
            print(time.monotonic())
            print('enter fertig')
    timer_sec = time.monotonic()



while True:
    # jetzt pro Button checken, ob gedrückt wurde oder nicht.
    if not(btn_1_pin.value) and not(btn_1_state):
        timeout()
        btn_1_state = True
        keyboard.press(Keycode.V)
        if debug:
            print('V an')
        time.sleep(sleep_time)
    if (btn_1_pin.value) and (btn_1_state):
        timeout()
        btn_1_state = False
        keyboard.release(Keycode.V)
        if debug:
            print('V aus')    
        time.sleep(sleep_time)


    if not(btn_2_pin.value) and not(btn_2_state):
        timeout()
        btn_2_state = True
        keyboard.press(Keycode.B)
        if debug:
            print('B an')
        time.sleep(sleep_time)
    if (btn_2_pin.value) and (btn_2_state):
        timeout()
        btn_2_state = False
        keyboard.release(Keycode.B)
        if debug:
            print('B aus')    
        time.sleep(sleep_time)

    if not(btn_3_pin.value) and not(btn_3_state):
        timeout()
        btn_3_state = True
        keyboard.press(Keycode.N)
        if debug:
            print('N an')
        time.sleep(sleep_time)
    if (btn_3_pin.value) and (btn_3_state):
        timeout()
        btn_3_state = False
        keyboard.release(Keycode.N)
        if debug:
            print('N aus')    
        time.sleep(sleep_time)
        
        
    if not(btn_4_pin.value) and not(btn_4_state):
        timeout()
        btn_4_state = True
        keyboard.press(Keycode.M)
        if debug:
            print('M an')
        time.sleep(sleep_time)
    if (btn_4_pin.value) and (btn_4_state):
        timeout()
        btn_4_state = False
        keyboard.release(Keycode.M)
        if debug:
            print('M aus')    
        time.sleep(sleep_time)
 
    if not(btn_5_pin.value) and not(btn_5_state):
        timeout()
        btn_5_state = True
        keyboard.press(Keycode.C)
        if debug:
            print('C an')
        time.sleep(sleep_time)
    if (btn_5_pin.value) and (btn_5_state):
        timeout()
        btn_5_state = False
        keyboard.release(Keycode.C)
        if debug:
            print('C aus')    
        time.sleep(sleep_time)
