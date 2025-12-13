import board
import displayio
import adafruit_imageload
import gc
import time
from digitalio import DigitalInOut, Direction

# 5 - way Switch
UP = DigitalInOut(board.SWITCH_UP)
DOWN = DigitalInOut(board.SWITCH_DOWN)
LEFT = DigitalInOut(board.SWITCH_LEFT)
RIGHT = DigitalInOut(board.SWITCH_RIGHT)
PRESS = DigitalInOut(board.SWITCH_PRESS)

print(gc.mem_free())

display = board.DISPLAY

# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("/images/pacman.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

pacman = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width = 2,
                            height = 2,
                            tile_width = 8,
                            tile_height = 8)

# Create a Group to hold the sprite
group = displayio.Group(scale=1)

# Add the sprite to the Group
group.append(pacman)

# Add the Group to the Display
display.show(group)

# Set sprite location
group.x = 40
group.y = 40

# Pacman open mouth right
def openRight():
    pacman[0] = 0
    pacman[1] = 1
    pacman[2] = 28
    pacman[3] = 29

def halfRight():
    pacman[0] = 2
    pacman[1] = 3
    pacman[2] = 30
    pacman[3] = 31

def openLeft():
    pacman[0] = 56
    pacman[1] = 57
    pacman[2] = 84
    pacman[3] = 85

def halfLeft():
    pacman[0] = 58
    pacman[1] = 59
    pacman[2] = 86
    pacman[3] = 87

def openUp():
    pacman[0] = 112
    pacman[1] = 113
    pacman[2] = 140
    pacman[3] = 141

def halfUp():
    pacman[0] = 114
    pacman[1] = 115
    pacman[2] = 142
    pacman[3] = 143

def openDown():
    pacman[0] = 168
    pacman[1] = 169
    pacman[2] = 196
    pacman[3] = 197

def halfDown():
    pacman[0] = 170
    pacman[1] = 171
    pacman[2] = 198
    pacman[3] = 199

def fullPac():
    pacman[0] = 4
    pacman[1] = 5
    pacman[2] = 32
    pacman[3] = 33

openRight()

direction = "none"

delay = 0.015

pixels = 4

def checkInput():
    global direction
    if UP.value == False:
        direction = "up"
    elif DOWN.value == False:
        direction = "down"
    elif LEFT.value == False:
        direction = "left"
    elif RIGHT.value == False:
        direction = "right"
    #print(direction)
    return(dir)

def edgeCheckRight():
    if group.x >= 296:
        return True

def edgeCheckLeft():
    if group.x <= 8:
        return True

def edgeCheckTop():
    if group.y <= 16:
        return True

def edgeCheckBottom():
    if group.y >= 216:
        return True

while True:
    checkInput()

    while direction == "right":
        if edgeCheckRight():
            direction = "none"
            break
        for f in [openRight, halfRight, fullPac, halfRight]:
            startx = group.x
            currx = startx
            while currx - startx < pixels:
                group.x += 1
                time.sleep(delay)
                currx = group.x
                checkInput()
            f()
            checkInput()
            
    while direction == "left":
        if edgeCheckLeft():
            direction = "none"
            break
        for f in [openLeft, halfLeft, fullPac, halfLeft]:
            startx = group.x
            currx = startx
            while abs(currx - startx) < pixels:
                group.x -= 1
                time.sleep(delay)
                currx = group.x
                checkInput()
            f()
            checkInput()

    while direction == "up":
        if edgeCheckTop():
            direction = "none"
            break
        for f in [openUp, halfUp, fullPac, halfUp]:
            starty = group.y
            curry = starty
            while abs(curry - starty) < pixels:
                group.y -= 1
                time.sleep(delay)
                curry = group.y
                checkInput()
            f()
            checkInput()

    while direction == "down":
        if edgeCheckBottom():
            direction = "none"
            break
        for f in [openDown, halfDown, fullPac, halfDown]:
            starty = group.y
            curry = starty
            while curry - starty < pixels:
                group.y += 1
                time.sleep(delay)
                curry = group.y
                checkInput()
            f()
            checkInput()