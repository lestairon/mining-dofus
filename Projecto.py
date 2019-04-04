import os, pyautogui, time
from PIL import ImageGrab, Image

x_pad = 254
y_pad = 42
bronze = {"color1" : (134, 90, 62), "color2" : (143, 98, 80), "color3" : (84, 41, 14), "color4" : (138, 96, 59), "color5" : (136, 94, 61)}
manganeso = {}
def Screencap():
    box = (x_pad+1, y_pad+1, x_pad+1088, y_pad+635)
    im = ImageGrab.grab(bbox=box)
    #im.save(os.environ['USERPROFILE'] + "\\screenshots\\sc.png", "PNG")
    return im

def MouseEvents(x, y):
    pyautogui.click(x = x_pad+x, y = y_pad+y)
    time.sleep(0.1)
    pyautogui.click(x = x_pad+x+38, y = y_pad+y+45)
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

def __main__():
    while True:
        x, y = detectMineral()
        if x != 0 and y != 0:
            MouseEvents(x, y)

#Screencap()
__main__()
