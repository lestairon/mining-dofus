from pynput.mouse import Controller, Button
from pynput import keyboard
import os, time
from PIL import ImageGrab, Image

x_pad = 254
y_pad = 42
current = set()
combinations = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='q')}
script = True

bronze = {"color1" : (134, 90, 62), "color2" : (143, 98, 80), "color3" : (84, 41, 14), "color4" : (138, 96, 59), "color5" : (136, 94, 61)}
manganeso = {}
def Screencap():
    box = (x_pad+1, y_pad+1, x_pad+1088, y_pad+635)
    im = ImageGrab.grab(bbox=box)
    #im.save(os.environ['USERPROFILE'] + "\\screenshots\\sc.png", "PNG")
    return im

def on_press(key):
    if key in combinations:
        current.add(key)
        global script
        if all(k in current for k in combinations):
            if script:
                script = False
                execute()
            else:
                script = True

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def MouseEvents(x, y):
    mouse = Controller()
    mouse.position = x_pad+x, y_pad+y
    mouse.click(Button.left, 1)
    time.sleep(0.1)
    mouse.move(38, 45)
    mouse.click(Button.left, 1)
    time.sleep(3)

def detectMineral():
    im = Screencap()
    w, h = im.size
    x_pos, y_pos = 0, 0
    n = 0
    for i in range(w):
        for j in reversed(range(h)):
            #print("x: " + str(i) +  " y: " + str(j))
            r,g,b = im.getpixel((i, j))
            if (r, g, b) in bronze.values() or (r, g, b) in manganeso.values():
                n += 1
                x_pos, y_pos = i, j
            if (n >= 3):
                break
    return x_pos, y_pos

def execute():
    global script
    while script:
        x, y = detectMineral()
        if x != 0 and y != 0:
            MouseEvents(x, y)
        if not script:
            break
    script = False
    print("xd")

def __main__():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

__main__()
