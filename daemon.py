import cec
import uinput
import time

u = uinput

KEYMAP = {
   0: u.KEY_ENTER,
   1: u.KEY_UP,
   2: u.KEY_DOWN,
   3: u.KEY_LEFT,
   4: u.KEY_RIGHT,
  13: u.KEY_BACK,
  68: u.KEY_PLAY,
  69: u.KEY_STOP,
  70: u.KEY_PAUSE,
  75: u.KEY_FASTFORWARD,
  76: u.KEY_REWIND,
 113: u.KEY_BLUE,
 114: u.KEY_RED,
 115: u.KEY_YELLOW,
 116: u.KEY_GREEN
}

cec.init()
device = uinput.Device(KEYMAP.values())

print("Ready")

def onkey(event, key, state):
  if state > 0:
    print("Got key", key, "state", state)
    device.emit_click(KEYMAP[key])

cec.add_callback(onkey, cec.EVENT_KEYPRESS)

while True:
 time.sleep(9e9)
